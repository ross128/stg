from django.conf.urls import include, url
from index import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$', views.main),
]
