from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ships.models import *
from map.util import get_map

@login_required
def shiplist(request):
	"""list of all owned ships"""
	ship_list = Ship.objects.filter(owner=request.user)
	return render(request, 'ships/list.html', {'ship_list': ship_list})

@login_required
def ship(request, ship_id):
	ship = get_object_or_404(Ship, pk=ship_id, owner=request.user)
	local_map = get_map( (ship.x, ship.y), 5)

	#get ships in sensor range
	ships_in_sensor_range_query = Ship.objects.filter(x__range=(ship.x-5, ship.x+5)).filter(y__range=(ship.y-5, ship.y+5))
	ships_in_sensor_range = {}
	for other_ship in ships_in_sensor_range_query:
		if not other_ship.y in ships_in_sensor_range:
			ships_in_sensor_range[other_ship.y] = {}
		if not other_ship.x in ships_in_sensor_range[other_ship.y]:
			ships_in_sensor_range[other_ship.y][other_ship.x] = [other_ship]
		else:
			ships_in_sensor_range[other_ship.y][other_ship.x].append(other_ship)
	return render(request, 'ships/ship.html', {
		'ship': ship,
		'local_map': local_map,
		'ships_in_sensor_range': ships_in_sensor_range,
		'ships_in_sector': ships_in_sensor_range_query.filter(x=ship.x).filter(y=ship.y).exclude(pk=ship.pk),
	})

@login_required
def move(request, ship_id):
	"""moves ship"""
	ship = get_object_or_404(Ship, pk=ship_id)

	try:
		jump = int(request.POST['jump'])
		if jump < 1:
			messages.error(request, "could not move ship")
		else:
			if 'up' in request.POST:
				ship.y -= jump
				messages.success(request, "moved up: %s" % jump)
			elif 'left' in request.POST:
				messages.success(request, "moved left: %s" % jump)
				ship.x -= jump
			elif 'right' in request.POST:
				messages.success(request, "moved right: %s" % jump)
				ship.x += jump
			elif 'down' in request.POST:
				messages.success(request, "moved down: %s" % jump)
				ship.y += jump
			ship.save()
	except Exception as e:
		messages.error(request, "could not move ship")
	return HttpResponseRedirect(reverse('ships:detail', args=(ship_id,)))

