from django.core.management.base import BaseCommand
from colony.models import Colony
import datetime

class Command(BaseCommand):
	"""executes tick computation"""
	help = 'Executes tick computation'

	def handle(self, *args, **options):
		# start the tick computation
		print("starting tick computation")
		starttime = datetime.datetime.now()

		#colony tick
		for colony in Colony.objects.all():
			print("[colony] {0.pk}: {0}".format(colony))
			colony.tick()

		# finish and measure time
		duration = datetime.datetime.now() - starttime
		print("tick computation finished, duration={0}".format(duration))

