# Django settings for stg project.

import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sh&amp;k@)5ryk^94j5!p**hnp+72*xcg*5xf#rcw4wl9tr6@ew)ro'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites', #XXX missing
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'index',
	'mainscreen',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware', #XXX new
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware', # XXX beeded?
)

ROOT_URLCONF = 'stg.urls'

# WSGI settings
WSGI_APPLICATION = 'stg.wsgi.application'

# Database settings
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
	}
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))

# Template settings
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
	os.path.abspath(os.path.join(BASE_DIR, 'templates')),
)

# Login settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/main/'

