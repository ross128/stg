from django.conf.urls import patterns, include, url
from colony import views

urlpatterns = patterns('colony.views',

	#field details
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/$', views.fielddetail, name='fielddetail'),

	#colony detail
	url(r'^(?P<colony_id>\d+)/$', views.colony, name='colony'),

	#list
	url(r'^$', views.colonylist, name='colonylist'),
)
