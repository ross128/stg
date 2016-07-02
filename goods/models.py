from django.db import models

class Good(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Stock(models.Model):
	goods = models.ManyToManyField(Good, through='GoodAssignment')

	def __str__(self):
		return "Stock {0.pk}".format(self)

class GoodAssignment(models.Model):
	good = models.ForeignKey(Good)
	stock = models.ForeignKey(Stock)
	count = models.IntegerField()

	class Meta:
		unique_together = ('stock', 'good')

	def __str__(self):
		return "Stock {0.stock} contains {0.count} items of {0.good}".format(self)
