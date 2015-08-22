from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property

class ShipClass(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Ship classes'

	def __str__(self):
		return "%s class" % self.name

class ShipProperty(models.Model):
	"""property assignable to modules"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Module(models.Model):
	"""modules to install into ships"""
	name = models.CharField(max_length=100)
	module_properties = models.ManyToManyField(ShipProperty, through='ModulePropertyAssignment')

	def __str__(self):
		return self.name

class ModulePropertyAssignment(models.Model):
	"""assignment of properties to modules"""
	module = models.ForeignKey(Module)
	module_property = models.ForeignKey(ShipProperty)
	value = models.FloatField()

	class Meta:
		unique_together = (('module', 'module_property'),)

	def __str__(self):
		return "Module {} has {} {}".format(self.module.name, self.value, self.module_property.name)

class Ship(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(User)
	shipclass = models.ForeignKey(ShipClass)
	modules = models.ManyToManyField(Module, through='ModuleAssignment')

	# position
	x = models.IntegerField()
	y = models.IntegerField()

	# compute (maximum) hull points
	@cached_property
	def hull(self):
		"""returns (maximum) hull points of the ship"""
		hull = 0.0
		for ma in self.moduleassignment_set.all():
			count = ma.count
			for prop in ModulePropertyAssignment.objects.filter(module=ma.module).filter(module_property__name__exact='hullpoints'):
				hull += count * prop.value
		return int(hull)

	def __str__(self):
		return "Ship: %s (%s class)" % (self.name, self.shipclass.name)

class ModuleAssignment(models.Model):
	ship = models.ForeignKey(Ship)
	module = models.ForeignKey(Module)
	count = models.PositiveSmallIntegerField()

	class Meta:
		unique_together = (('ship', 'module'),)

	def __str__(self):
		return "Ship {} has {} modules of type {}".format(self.ship.name, self.count, self.module.name)

