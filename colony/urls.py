from django.conf.urls import patterns, include, url
from colony import views

urlpatterns = patterns('colony.views',

	#build building
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/build/$', views.BuildBuilding.as_view(), name='build'),

	#field details
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/$', views.FieldDetail.as_view(), name='fielddetail'),

	#colony detail
	url(r'^(?P<colony_id>\d+)/$', views.colony, name='colony'),

	#list
	url(r'^$', views.colonylist, name='list'),
)
