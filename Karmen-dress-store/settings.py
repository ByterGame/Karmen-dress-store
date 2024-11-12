from pathlib import Path
import os
import sys
sys.path.append("Karmen-dress-store")
from validators import LengthValidator, CharValidator, VariousSymbolsValidator
import re

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-7$&ue%r@0och!@gbjq@xu2ofx&k32(1ju2w2%1=b(%r_ex@mh!'

DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost/', 'http://127.0.0.1/', 'https://35db-82-162-122-185.ngrok-free.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'users',
    'yoomoney',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Karmen-dress-store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Karmen-dress-store.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'validators.LengthValidator',
    },
    {
        'NAME': 'validators.VariousSymbolsValidator',
    },
    {
        'NAME': 'validators.CharValidator',
    },
]

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]

LANGUAGE_CODE = 'en-uc'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
