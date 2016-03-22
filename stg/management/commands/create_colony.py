from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from colony.models import Colony, Field, FieldAssignment

class Command(BaseCommand):
	"""creates colony for given user"""
	help = 'creates colony for given user'

	def add_arguments(self, parser):
		parser.add_argument('user_id', type=int)

	def handle(self, *args, **options):
		try:
			user = User.objects.get(pk=options['user_id'])
		except User.DoesNotExist:
			return 'user with given id does not exist!'

		c = Colony()
		c.name = 'New Colony'
		c.owner = user
		c.save()

		space = Field.objects.get(pk=7)
		grass = Field.objects.get(pk=1)
		ground = Field.objects.get(pk=8)

		#10 columns
		for col in range(10):
			for row in range(2+6+2):
				f = FieldAssignment()
				if row < 2:
					#create 2 rows of space
					f.field = space
				elif row < 8:
					#then 6 rows of grass
					f.field = grass
				else:
					#then 2 rows of underground dirt
					f.field = ground

				f.colony = c
				f.x = col
				f.y = row
				f.save()
