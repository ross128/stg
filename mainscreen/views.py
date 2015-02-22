from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def mainscreen(request):
	"""docstring for mainscreen"""
	return render(request, 'mainscreen/mainscreen.html')

