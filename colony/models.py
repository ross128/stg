from django.db import models
from django.contrib.auth.models import User

class Colony(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User)

	class Meta(object):
		verbose_name_plural = "Colonies"

	def __unicode__(self):
		"""prints description"""
		return self.name


