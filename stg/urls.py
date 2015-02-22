from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#login and logout
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},  name='logout'),


	# admin interface
	url(r'^admin/', include(admin.site.urls)),

	#mainscreen
	url(r'^main/', include('mainscreen.urls')),

	#colony
	url(r'^colony/', include('colony.urls')),

	url(r'^$', include('index.urls')),
)

# serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

