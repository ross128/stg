from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from colony.models import Colony
from django.core.exceptions import ObjectDoesNotExist

@login_required
def colonylist(request):
	"""list of all owned colonies"""
	colony_list = Colony.objects.filter(owner=request.user)
	return render(request,'colony/colonylist.html',{'colony_list': colony_list})

@login_required
def colony(request,colony_id):
	"""a detailled view of the colony"""
	try:
		colony = Colony.objects.get(pk=colony_id,owner=request.user)
	except ObjectDoesNotExist:
		colony = None

	#extract maximum fieldsizes
	surfacesize = reduce(
			lambda a,b: {'x': max(a['x'],b['x']), 'y': max(a['y'],b['y'])} ,
			( {'x': field.x, 'y': field.y} for field in colony.fieldassignment_set.all() ),
			{'x': 0, 'y': 0}
		)

	surface = {}
	for y in xrange(surfacesize['y'] + 1):
		surface[y] = {}
		for x in xrange(surfacesize['x'] + 1):
			surface[y][x] = {}

	for field in colony.fieldassignment_set.all():
		surface[field.y][field.x]['field'] = field

	return render(request,'colony/colony.html', {
		'colony': colony,
		'surface': surface,
	})
