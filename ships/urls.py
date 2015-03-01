from django.conf.urls import patterns, include, url
from ships import views

urlpatterns = patterns('ships.views',

   # #field details
   # url(r'^(?P<colony_id>\d+)/field/(?P<x>\d+)/(?P<y>\d+)/$', views.fielddetail, name='fielddetail'),

   # ship detail
   url(r'^(?P<ship_id>\d+)/$', views.ship, name='detail'),

	# list
	url(r'^$', views.shiplist, name='list'),
)

