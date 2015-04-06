from django.db import models

class FieldType(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Field(models.Model):
	fieldtype = models.ForeignKey(FieldType)
	x = models.IntegerField()
	y = models.IntegerField()

	class Meta(object):
		index_together = ["x", "y"]
		unique_together = ["x", "y"]

	def __str__(self):
		return "%s at (%d, %d)" % (self.fieldtype.name, self.x, self.y)

