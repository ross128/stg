from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.functional import cached_property
from goods.models import Stock

class Field(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Colony(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	fields = models.ManyToManyField(Field, through='FieldAssignment')
	stock = models.OneToOneField(Stock)
	energy = models.PositiveSmallIntegerField(default=0)
	residents = models.PositiveSmallIntegerField(default=0)

	class Meta(object):
		verbose_name_plural = "Colonies"

	def __str__(self):
		return self.name

	def collect_building_properties(self, property_name):
		"""collect sum of all building properties on the surface"""
		result = 0

		for fa in self.fieldassignment_set.all():
			ba = fa.buildingassignment_set.first()
			if ba is not None and ba.is_active:
				#there is an active building on this field
				for property_assignment in ba.building.buildingpropertyassignment_set.filter(building_property__name__exact=property_name):
					result += property_assignment.value

		return result

	@cached_property
	def living_quarters(self):
		"""returns number of living quarters on the colony"""
		return int(self.collect_building_properties('living_quarters'))

	@cached_property
	def max_energy(self):
		"""returns energy capacity of colony"""
		return int(self.collect_building_properties('eps'))

	@cached_property
	def workers(self):
		"""returns number of required workers of colony"""
		return int(self.collect_building_properties('workers'))

	def tick(self):
		"""compute the tick for the colony"""
		#add residents to colony
		remaining = self.living_quarters - self.residents
		if remaining > 0:
			immigration = max(1, int(remaining/2))
			self.residents += immigration
		elif remaining < 0:
			#emigration
			self.residents = self.living_quarters

		#loop through all buildings
		remaining_workers = self.residents
		for fa in self.fieldassignment_set.all():
			ba = fa.buildingassignment_set.first()

			if ba is None:
				#no building on this field
				continue

			if not ba.is_active:
				#building is deactivated or not built yet
				continue

			if self.energy + ba.building.production_energy < 0:
				#energy requirements not met: deactivate building
				ba.active = False
				ba.save()
				continue

			if not ba.building.production.can_produce(self.stock):
				#not enough resources available for this building
				ba.active = False
				ba.save()
				continue

			workers_qry = ba.building.buildingpropertyassignment_set.filter(building_property__name__exact='workers').first()
			workers = workers_qry.value if workers_qry else 0
			if remaining_workers - workers < 0:
				#not enough free workers available
				ba.active = False
				ba.save()
				continue

			#execute building production
			remaining_workers -= workers
			self.stock += ba.building.production
			self.energy += ba.building.production_energy

		#cap energy production
		self.energy = min(self.max_energy, self.energy)
		self.save()

@receiver(pre_save, sender=Colony)
def add_empty_stock(sender, instance, **kwargs):
	if not instance.stock_id:
		stock = Stock.objects.create()
		stock.save()
		instance.stock = stock

class FieldAssignment(models.Model):
	colony = models.ForeignKey(Colony)
	field = models.ForeignKey(Field)
	x = models.PositiveSmallIntegerField()
	y = models.PositiveSmallIntegerField()

	class Meta:
		unique_together = (('colony', 'x', 'y'),)
		ordering = ['y','x']

	def __str__(self):
		return "%s has %s at (%d,%d)" % (self.colony.name,self.field.name,self.x,self.y)

class BuildingProperty(models.Model):
	"""defines properties of specific buildings"""
	name = models.CharField(max_length=100)

	class Meta(object):
		verbose_name_plural = "Building Properties"

	def __str__(self):
		return self.name

class Building(models.Model):
	"""building"""
	name = models.CharField(max_length = 200)
	usable_fields = models.ManyToManyField(Field, through='BuildingConstruction')

	build_time = models.DurationField()
	building_cost = models.OneToOneField(Stock, related_name='building_cost')
	building_energy_cost = models.PositiveSmallIntegerField(default=0)

	production = models.OneToOneField(Stock, related_name='building_production')
	production_energy = models.SmallIntegerField(default=0)

	building_properties = models.ManyToManyField(BuildingProperty, through='BuildingPropertyAssignment')

	def __str__(self):
		return self.name

class BuildingPropertyAssignment(models.Model):
	building = models.ForeignKey(Building)
	building_property = models.ForeignKey(BuildingProperty)
	value = models.FloatField()

	class Meta:
		unique_together = (('building', 'building_property'),)

	def __str__(self):
		return "Building {} has {} {}".format(self.building.name, self.value, self.building_property.name)

class BuildingConstruction(models.Model):
	"""describes which building can be built on which field"""
	building = models.ForeignKey(Building)
	field = models.ForeignKey(Field)

	def __str__(self):
		return "Building %s can be built on field %s" % (self.building.name, self.field.name)

class BuildingAssignment(models.Model):
	"""assigns a building to a field on a colony"""
	field = models.ForeignKey(FieldAssignment)
	building = models.ForeignKey(Building)
	construction_finished = models.DateTimeField(default=timezone.now)

	active = models.BooleanField(default=True)

	@property
	def is_active(self):
		"""returns True iff building is activated and construction is finished"""
		return self.active and not self.under_construction

	@property
	def construction_progress(self):
		"""returns the construction progress in percent"""
		return 100.0*min(1, (1 - (self.construction_finished - timezone.now())/self.building.build_time))

	@property
	def under_construction(self):
		"""returns True iff building is under construction"""
		return timezone.now() < self.construction_finished

	def __str__(self):
		return "%sBuilding '%s' on field %s (%d, %d)" % ("Construction until " + str(self.construction_finished) + " " if self.construction_finished > timezone.now() else "", self.building.name, self.field.field.name, self.field.x, self.field.y)

