from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
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

	class Meta(object):
		verbose_name_plural = "Colonies"

	def __str__(self):
		return self.name

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

class Building(models.Model):
	"""building"""
	name = models.CharField(max_length = 200)
	usable_fields = models.ManyToManyField(Field, through='BuildingConstruction')
	build_time = models.DurationField()
	building_cost = models.OneToOneField(Stock, related_name='building_cost')
	production = models.OneToOneField(Stock, related_name='building_production')

	def __str__(self):
		return self.name

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

