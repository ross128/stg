from django.conf.urls import patterns, include, url
from colony import views

urlpatterns = patterns('colony.views',

	#colony detail
	url(r'(?P<colony_id>\d+)/', views.colony, name='colony'),

	#list
	url(r'', views.colonylist, name='colonylist'),
)
