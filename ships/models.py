from django.db import models
from django.contrib.auth.models import User

class ShipClass(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Ship classes'

	def __str__(self):
		return "%s class" % self.name

class Module(models.Model):
	"""modules to install into ships"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Ship(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(User)
	shipclass = models.ForeignKey(ShipClass)
	modules = models.ManyToManyField(Module, through='ModuleAssignment')

	# position
	x = models.IntegerField()
	y = models.IntegerField()

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

