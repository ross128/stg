from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ships.models import *

@login_required
def shiplist(request):
	"""list of all owned ships"""
	ship_list = Ship.objects.filter(owner=request.user)
	return render(request, 'ships/list.html', {'ship_list': ship_list})

@login_required
def ship(request, ship_id):
	ship = get_object_or_404(Ship, pk=ship_id)
	return render(request, 'ships/ship.html', {'ship': ship})

