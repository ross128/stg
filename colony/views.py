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
	return render(request,'colony/colony.html', {'colony': colony})
