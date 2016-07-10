from django.db import models, transaction

class Good(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Stock(models.Model):
	goods = models.ManyToManyField(Good, through='GoodAssignment')

	def __le__(self, other):
		for ga in self.goodassignment_set.all():
			other_ga = other.goodassignment_set.filter(good=ga.good)
			if other_ga.count() < 1:
				#other stock does not contain this good
				return False

			if other_ga.first().count < ga.count:
				#other stock has lower number of goods
				return False
		return True

	def add_delta(self, other, negative=False):
		"""adds or subtracts (iff negative==True) a stock to another stock"""
		sign = -1 if negative else 1

		with transaction.atomic():
			for ga in other.goodassignment_set.all():
				self_ga = self.goodassignment_set.filter(good=ga.good)

				if self_ga.count() < 1:
					#this stock does not contain this good

					if sign*ga.count < 0:
						#this would create a negative count
						raise Exception("could not add resource to this stock")

					#add new ressource
					if ga.count == 0:
						#nothing to do
						continue

					#create new goodassignment for this stock
					self.goodassignment_set.create(good=ga.good, count=sign*ga.count)

				else:
					#good is already in this stock

					self_ga = self_ga.first()
					if self_ga.count + sign*ga.count < 0:
						#this would create a negative count
						raise Exception("could not add resource to this stock")

					#add resource
					if self_ga.count + sign*ga.count == 0:
						self_ga.delete()
					else:
						self_ga.count += sign*ga.count
						self_ga.save()
		return self

	def __isub__(self, other):
		"""implements Stock -= Stock"""
		return self.add_delta(other, negative=True)

	def __iadd__(self, other):
		"""implements Stock += Stock"""
		return self.add_delta(other)

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
