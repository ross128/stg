from django.db import models
from django.contrib.auth.models import User
import timedelta

class Field(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		"""prints desription"""
		return self.name

class Colony(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User)
	fields = models.ManyToManyField(Field, through='FieldAssignment')

	class Meta(object):
		verbose_name_plural = "Colonies"

	def __unicode__(self):
		"""prints description"""
		return self.name

class FieldAssignment(models.Model):
	colony = models.ForeignKey(Colony)
	field = models.ForeignKey(Field)
	x = models.PositiveSmallIntegerField()
	y = models.PositiveSmallIntegerField()

	class Meta:
		unique_together = (('colony', 'x', 'y'),)
		ordering = ['y','x']

	def __unicode__(self):
		"""prints description"""
		return "%s has %s at (%d,%d)" % (self.colony.name,self.field.name,self.x,self.y)

class Building(models.Model):
	"""building"""
	name = models.CharField(max_length = 200)
	usable_fields = models.ManyToManyField(Field, through='BuildingConstruction')
	build_time = timedelta.TimedeltaField()

	def __unicode__(self):
		"""prints description"""
		return self.name

class BuildingConstruction(models.Model):
	"""describes which building can be built on which field"""
	building = models.ForeignKey(Building)
	field = models.ForeignKey(Field)

	def __unicode__(self):
		"""prints description"""
		return "Building %s can be built on field %s" % (self.building.name, self.field.name)

class BuildingAssignment(models.Model):
	"""assigns a building to a field on a colony"""
	field = models.ForeignKey(FieldAssignment)
	building = models.ForeignKey(Building)

	def __unicode__(self):
		"""prints description"""
		return "Building %s on field %s" % (self.building.name,self.field.name)
