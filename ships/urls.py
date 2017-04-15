from django.conf.urls import include, url
from ships import views

urlpatterns = [

	# ship movement
	url(r'^(?P<ship_id>\d+)/move/$', views.move, name='move'),

	# ship detail
	url(r'^(?P<ship_id>\d+)/$', views.ship, name='detail'),

	# list
	url(r'^$', views.shiplist, name='list'),
]

