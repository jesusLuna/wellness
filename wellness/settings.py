"""
Django settings for wellness project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ugettext = lambda s: s  # dummy ugettext function, as said on django docs

WELLNESS_BASEDIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(WELLNESS_BASEDIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=8i9&*taus)$l&ym@0_&nx-+5)!nh6b3hhqbf2+&r6x6-h1k&w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djng',
    'facturas',
)

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

ROOT_URLCONF = 'wellness.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wellness.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wellness',                      # Or path to database file if using sqlite3.
        'USER': 'wellness',                      # Not used with sqlite3.
        'PASSWORD': '1111',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'
CURRENCY = 'EUR'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL_PREFIX = 'static'
STATIC_URL = '/%s/' % STATIC_URL_PREFIX

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, STATIC_URL_PREFIX),
)