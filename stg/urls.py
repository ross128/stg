from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#login and logout
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},  name='logout'),


	# admin interface
	url(r'^admin/', include(admin.site.urls)),

	#mainscreen
	url(r'^main', include('mainscreen.urls')),

	url(r'', include('index.urls')),
)
