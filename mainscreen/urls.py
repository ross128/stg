from django.conf.urls import patterns, include, url
from mainscreen import views

urlpatterns = patterns('mainscreen.views',
	#mainscreen
	url(r'^$', 'mainscreen', name='mainscreen'),
)
