from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.site.site_title = 'STG Administration'
admin.site.site_header = 'STG Administration'
admin.site.site_url = '/main/'

urlpatterns = [
	#login and logout
	url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': '/'},  name='logout'),

	# admin interface
	url(r'^admin/', include(admin.site.urls)),

	#mainscreen
	url(r'^main/', include('mainscreen.urls', namespace='main')),

	#colony
	url(r'^colony/', include('colony.urls', namespace='colony')),

	#ships
	url(r'^ships/', include('ships.urls', namespace='ships')),

	#index page
	url(r'^', include('index.urls')),
]

# serve static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

