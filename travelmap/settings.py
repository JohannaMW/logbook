"""
Django settings for travelmap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0i$ggc*l$9)abp3g@uw9fo0ny55m8#3_fy1jhkl9!r-ud69&&^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'logbook',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'travelmap.urls'

WSGI_APPLICATION = 'travelmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_ACCESS_KEY_ID = "AKIAIM2TWT4MAXQVFMTQ"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# Use Amazon S3 for storage for uploaded media files.

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Use Amazon S3 and RequireJS for static files storage.

STATICFILES_STORAGE = "require_s3.storage.OptimizedCachedStaticFilesStorage"

# Amazon S3 settings.
#
AWS_SECRET_ACCESS_KEY = "+tRSN46eVMZ1SI1uzn7te5KXfrxuMddRovZ/1fWn"
#
AWS_STORAGE_BUCKET_NAME = "myfirstbucket1503"

AWS_AUTO_CREATE_BUCKET = True

AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}

AWS_S3_FILE_OVERWRITE = False

AWS_QUERYSTRING_AUTH = False

AWS_S3_SECURE_URLS = True

AWS_REDUCED_REDUNDANCY = False

AWS_IS_GZIPPED = False

BOTO_S3_BUCKET = "myfirstbucket1503"

STATIC_URL = "https://myfirstbucket1503.s3.amazonaws.com/".format(
    bucket_name = AWS_STORAGE_BUCKET_NAME,
)

STATIC_URL = '/static/'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))

try:
    from local_settings import *
except ImportError:
    pass