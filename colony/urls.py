from django.conf.urls import include, url
from colony import views

urlpatterns = [

	#switch building
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/switch/$', views.SwitchBuilding.as_view(), name='switch'),

	#build building
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/build/$', views.BuildBuilding.as_view(), name='build'),

	#field details
	url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/$', views.FieldDetail.as_view(), name='fielddetail'),

	#colony detail
	url(r'^(?P<colony_id>\d+)/$', views.colony, name='colony'),

	#list
	url(r'^$', views.colonylist, name='list'),
]
