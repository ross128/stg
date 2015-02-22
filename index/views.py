from django.http import HttpResponse
from django.shortcuts import render

def main(request):
	"""docstring for mainscreen"""
	return render(request, 'index/index.html')

