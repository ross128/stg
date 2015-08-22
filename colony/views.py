from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from colony.models import Colony, Building
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

@login_required
def fielddetail(request, colony_id, x, y):
	"""get detail view of field"""
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
