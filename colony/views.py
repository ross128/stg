from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def colonylist(request):
	"""docstring for mainscreen"""
	return render_to_response('colony/colonylist.html')

# @login_required
def colony(request,colony_id):
	"""docstring for colony"""
	return render_to_response('colony/colony.html')
