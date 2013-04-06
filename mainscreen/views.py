from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def mainscreen(request):
	"""docstring for mainscreen"""
	return render_to_response('mainscreen/mainscreen.html')
