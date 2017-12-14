import os
import sys
import re


# It is used for relative settings elsewhere.
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'xd)%*l7@o@3q+=^&3%i&pz0p7-bw6!b65pig(fn)^1wha1en8k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.50', 'localhost', '172.16.104.126', '127.0.0.1']


# Application definition

LIVESTOCK_APPS = (
    'liveapp',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',


    # gis
    'rest_framework_swagger',
    'django.contrib.gis',
    'phonenumber_field',
    'leaflet',
    'djgeojson',
    'bootstrap3',
    'bootstrap_toolkit',
    'rest_framework',
    'rest_framework_gis',
    'africastalking'
) + LIVESTOCK_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


ROOT_URLCONF = 'livestock.urls'

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
# )


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'livestock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'livestock',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

GEOS_LIBRARY_PATH = 'C:/Users/deryq/imp/myenv/Lib/site-packages/osgeo/geos_c.dll'
GDAL_LIBRARY_PATH = 'C:/Users/deryq/imp/myenv/Lib/site-packages/osgeo/gdal202.dll'
new_path = 'C:/Program Files/PostgreSQL/9.5/gdal-data'
os.environ['GDAL_DATA'] = new_path
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = MEDIA_DIR


# PHONENUMBER_DEFAULT_REGION = 'INTERNATIONAL'
# PHONENUMBER_DB_FORMAT = 'E164'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-0.4535, 36.7568),
    'DEFAULT_ZOOM': 14,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'TILES': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',

    # 'OVERLAYS': [
    #     ('Watercolor',
    #      'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png',
    #      'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
    #      <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> \
    #      &mdash; Map data &copy; \
    #      <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
    #      <a href="http://creativecommons.org/licenses/by-sa/2.0/"> \
    #      CC-BY-SA</a>'),

    #     ('Toner Lite',
    #      'http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png',
    #      'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
    #      <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> \
    #      &mdash; Map data &copy; \
    #      <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
    #      <a href="http://creativecommons.org/licenses/by-sa/2.0/"> \
    #      CC-BY-SA</a>'),
    # ],

    # 'PLUGINS': {
    #     'esri-leaflet': {
    #         'js': 'lib/js/esri-leaflet.js',
    #         'auto-include': True,
    #     },
    #     'leaflet-fullscreen': {
    #         'css': 'lib/css/leaflet.fullscreen.css',
    #         'js': 'lib/js/Leaflet.fullscreen.min.js',
    #         'auto-include': True,
    #     },
    #     'leaflet-opacity': {
    #         'css': 'lib/css/Control.Opacity.css',
    #         'js': 'lib/js/Control.Opacity.js',
    #         'auto-include': True,
    #     },
    #     'leaflet-navbar': {
    #         'css': 'lib/css/Leaflet.NavBar.css',
    #         'js': 'lib/js/Leaflet.NavBar.js',
    #         'auto-include': True,
    #     },
    #     'leaflet-measure': {
    #         'css': 'lib/css/leaflet-measure.css',
    #         'js': 'lib/js/leaflet-measure.js',
    #         'auto-include': True,
    #     },
    # },
    # 'SRID': 3857,
    # 'RESET_VIEW': False

    # 'ATTRIBUTION_PREFIX': 'Powered by django-leaflet'
}

# if not DEBUG_STATIC:
#     # if not DEBUG_STATIC, use minified css and js
#     LEAFLET_CONFIG['PLUGINS'] = {
#         'leaflet-plugins': {
#             'js': 'lib/js/leaflet-plugins.min.js',
#             'css': 'lib/css/leaflet-plugins.min.css',
#             'auto-include': True,
#         }
#     }


# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}


# TWILIO_ACCOUNT_SID = 'ACb335a38990ac7be5fddc7e72a23312e0'
# TWILIO_AUTH_TOKEN = '430932c2b2de56fbfe8629ba78588447'
# DJANGO_TWILIO_FORGERY_PROTECTION = False
# DJANGO_TWILIO_BLACKLIST_CHECK = True
