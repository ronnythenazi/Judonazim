"""
Django settings for judonazim project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
# upload large files usuefyl link https://justdjango.com/blog/how-to-upload-large-files


import os
#import boto3
from django.core.management.utils import get_random_secret_key
from pathlib import Path
import sys
import dj_database_url
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") #or get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get("DEBUG")) == "1"



# Application definition
if DEBUG:
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        #personal
        'blog',
        #thirdparty
        'storages',
        'boto3',
        'ckeditor',
        'magazine',



    ]
else:
    INSTALLED_APPS = [
        #'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        #personal
        'blog',
        #thirdparty
        'boto3',
        'storages',
        'ckeditor',
        'magazine',

    ]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'judonazim.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),

        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'judonazim.wsgi.application'
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


DEFAULT_AUTO_FIELD='django.db.models.AutoField'

"""

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_USER is not None
    and POSTGRES_HOST is not None
    and POSTGRES_PORT is not None
)

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }
"""


"""
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
"""

if not DEBUG:
    AWS_ACCESS_KEY_ID = str(os.environ.get("AWS_ACCESS_KEY_ID"))
    AWS_SECRET_ACCESS_KEY = str(os.environ.get("AWS_SECRET_ACCESS_KEY"))
    AWS_STORAGE_BUCKET_NAME = str(os.environ.get("AWS_STORAGE_BUCKET_NAME"))
    AWS_S3_ENDPOINT_URL = "https://ronnythenazi.fra1.digitaloceanspaces.com"
    AWS_LOCATION = f"https://{str(AWS_STORAGE_BUCKET_NAME)}fra1.digitaloceanspaces.com"
    #AWS_DEFAULT_ACL = 'public-read'


    DEFAULT_FILE_STORAGE = 'judonazim.cdn.MediaStorage'
    AWS_S3_OBJECT_PARAMETERS = {
      "CacheControl": "max-age=86400",
    }







#AWS_LOCATION =  "https://ronnythenazi.fra1.digitaloceanspaces.com" #f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com"


if DEBUG:
    MEDIA_URL = '/'
    MEDIA_ROOT = os.path.join(BASE_DIR, '')
else:
    """
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    """
    MEDIA_URL = AWS_S3_ENDPOINT_URL +'/'
    MEDIA_ROOT = 'media/'


STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'blog', 'static'),
      )
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')



#https://ronnythenazi.fra1.digitaloceanspaces.com

"""
# your_app/settings.py
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'width': '100%'
    },
}
"""

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        #'height' : '100%',
    },
}

ALLOWED_HOSTS = []

if not DEBUG:
    #ALLOWED_HOSTS = ['127.0.0.1']
    ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTS")]

#https://dev.to/shantanu_jana/how-to-preview-image-before-uploading-in-javascript-1f6g
#EFEFEF
