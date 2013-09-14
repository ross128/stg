from django.db import models
from django.contrib.auth.models import User

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
	# building = models.ForeignKey(Building)

	def __unicode__(self):
		"""prints description"""
		return "%s has %s" % (self.colony.name,self.field.name)

