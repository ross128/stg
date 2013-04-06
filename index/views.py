from django.http import HttpResponse
from django.shortcuts import render_to_response

def main(request):
	"""docstring for mainscreen"""
	return render_to_response('index/index.html')
