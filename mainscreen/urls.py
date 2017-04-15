from django.conf.urls import include, url
from mainscreen import views

urlpatterns = [
	#mainscreen
	url(r'^$', views.mainscreen, name='mainscreen'),
]
