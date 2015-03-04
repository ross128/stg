from django.db import models
from django.contrib.auth.models import User

class ShipClass(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s class" % self.name

class Ship(models.Model):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(User)
	shipclass = models.ForeignKey(ShipClass)

	# position
	x = models.IntegerField()
	y = models.IntegerField()

	def __unicode__(self):
		return "Ship: %s (%s class)" % (self.name, self.shipclass.name)

