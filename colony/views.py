from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.utils import timezone
from django.utils.decorators import method_decorator
from colony.models import Colony, Building, BuildingAssignment, BuildingConstruction
from functools import reduce

@login_required
def colonylist(request):
	"""list of all owned colonies"""
	colony_list = Colony.objects.filter(owner=request.user)
	return render(request,'colony/colonylist.html',{'colony_list': colony_list})

@login_required
def colony(request, colony_id):
	"""a detailled view of the colony"""
	colony = get_object_or_404(Colony, pk=colony_id, owner=request.user)

	#extract maximum fieldsizes
	surfacesize = reduce(
			lambda a,b: {'x': max(a['x'],b['x']), 'y': max(a['y'],b['y'])} ,
			( {'x': field.x, 'y': field.y} for field in colony.fieldassignment_set.all() ),
			{'x': 0, 'y': 0}
		)

	surface = {}
	for y in range(surfacesize['y'] + 1):
		surface[y] = {}
		for x in range(surfacesize['x'] + 1):
			surface[y][x] = {}

	for field in colony.fieldassignment_set.all():
		surface[field.y][field.x]['field'] = field
		building = field.buildingassignment_set.first()
		if building:
			surface[field.y][field.x]['building'] = building

	return render(request,'colony/colony.html', {
		'colony': colony,
		'surface': surface,
	})

class FieldDetail(LoginRequiredMixin, View):
	"""get detail view of field"""

	def get(self, request, colony_id, x, y):
		colony = get_object_or_404(Colony, pk=colony_id, owner=request.user)
		field = colony.fieldassignment_set.filter(x=int(x), y=int(y)).first()
		building = field.buildingassignment_set.first()

		#retrieve building options
		buildings = field.field.buildingconstruction_set.all()

		return render(request,'colony/fielddetail.html', {
			'field': field,
			'building': building,
			'buildings': buildings,
		})

class SwitchBuilding(LoginRequiredMixin, View):
	"""activate or deactivate building"""
	def post(self, request, colony_id, x, y):
		colony = get_object_or_404(Colony, pk=colony_id, owner=request.user)
		fa = colony.fieldassignment_set.filter(x=int(x), y=int(y)).first()
		ba = fa.buildingassignment_set.first()

		if ba:
			ba.active = not ba.active
			ba.save()

			messages.info(request, "building {0} has been {1}".format(ba.building, "activated" if ba.active else "deactivated"))

		return HttpResponseRedirect(reverse('colony:colony', args=(colony_id,)))

class BuildBuilding(LoginRequiredMixin, View):
	"""build building"""

	def post(self, request, colony_id, x, y):
		colony = get_object_or_404(Colony, pk=colony_id, owner=request.user)
		fa = colony.fieldassignment_set.filter(x=int(x), y=int(y)).first()

		if fa.buildingassignment_set.first():
			messages.error(request, 'building already exists')
		else:
			try:
				building = Building.objects.get(pk=int(request.POST['build']))
			except Building.DoesNotExist:
				messages.error(request, "building does not exist")
				return HttpResponseRedirect(reverse('colony:fielddetail', args=(colony_id, x, y)))

			#can be build on this field?
			bc = BuildingConstruction.objects.filter(field=fa.field, building=building)
			if bc:
				#TODO check if you have enough energy
				if colony.energy >= building.building_energy_cost:

					#check if enough ressources are available
					if building.building_cost <= colony.stock:
						#deduct building ressources from colony stock
						colony.stock -= building.building_cost

						#deduct energy
						colony.energy -= building.building_energy_cost
						colony.save()

						#build
						ba = BuildingAssignment()
						ba.building = building
						ba.field = fa
						ba.construction_finished = timezone.now() + building.build_time
						ba.save()

						messages.info(request, "construction of {0} has been started".format(building))
					else:
						messages.error(request, "not enough ressources available")
				else:
					messages.error(request, "not enough energy available")

			else:
				messages.error(request, "building {0} cannot be build on {1}".format(building, fa.field))

		return HttpResponseRedirect(reverse('colony:colony', args=(colony_id,)))
