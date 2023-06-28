"""
Django settings for FirstTestProject project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--w)28tb5=4+z9j^x%oo1xm$41ff-@rj5ryq3py$h%3zt0^eifn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local app
    'accounts',
    'home',
    'reporter',
    'django.contrib.gis',

    # global app
    'captcha',
    'leaflet',

    # 'location_field.apps.DefaultConfig',
    # 'location_field.apps.DefaultConfig',
    # 'location_field',

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

ROOT_URLCONF = 'FirstTestProject.urls'

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

WSGI_APPLICATION = 'FirstTestProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": str(os.getenv("POSTGRES_DB_NAME", "gis")),
        "USER": str(os.getenv("POSTGRES_USER", "gis")),
        "PASSWORD": str(os.getenv("POSTGRES_PASSWORD", "gis")),
        "HOST": str(os.getenv("POSTGRES_HOST", "db")),
        "PORT": 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/medias/'

MEDIA_ROOT = 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'accounts.User'

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '47565f25e47ad6'
EMAIL_HOST_PASSWORD = '6960240a459ab9'
EMAIL_PORT = '2525'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RECAPTCHA_PUBLIC_KEY = '6LeVAIYmAAAAAFyPB-4T8NqqPWuV_LWwjFWrE6gL'
RECAPTCHA_PRIVATE_KEY = '6LeVAIYmAAAAAJvY5o7TzD5thHNisNMfLS03INIE'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-.023, 36.87),
    'DEFAULT_ZOOM': 5,
    # 'MAX_ZOOM': 30,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    # 'ATTRIBUTION_PREFIX': 'Inspired by Life in GIS'
}
