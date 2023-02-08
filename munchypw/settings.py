"""
Django settings for munchypw project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$zlasrofx2^cfvml3az_d(b%xrs5upigh$0kit8zzph)7qai=6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://munchysecurealpha.adaptable.app','https://cs947939-congenial-space-doodle-qprwjwprj7cxwg4-8000.preview.app.github.dev']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "password",
    "allauth",
    'allauth.account',
'allauth.socialaccount',
 'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    # Configure the django-otp package.
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',

    # Enable two-factor auth.
    'allauth_2fa',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'django_otp.middleware.OTPMiddleware',
    'allauth_2fa.middleware.AllauthTwoFactorMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "munchypw.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "munchypw.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DB_PW2 = os.environ.get('DB_PW')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_CONFIG = os.environ.get("DB_CONFIG")
if DB_CONFIG =="Dev/Pro":
    DATABASES = {
    "default": {
               'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME, 
        'USER': DB_USERNAME,
        'PASSWORD': DB_PW2,

        'HOST': DB_HOST,
        'PORT': '5432',
    }
}
else:
     DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': 'coding986532',
    'PASSWORD': 'hPwipzbog8v2',
    'HOST': 'ep-square-darkness-178541.us-east-2.aws.neon.tech',
    'PORT': '5432',
  },
  
}







# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
  
]
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ACCOUNT_ADAPTER = 'allauth_2fa.adapter.OTPAdapter'
SITE_ID = 2
DEFAULT_FILE_STORAGE = 'password.s3.MediaStorage'
AWS_S3_REGION_NAME = 'us-west-004'
AWS_S3_ENDPOINT_URL = 'https://s3.us-west-004.backblazeb2.com'
AWS_ACCESS_KEY_ID = '004a9e81991c2860000000001'
AWS_SECRET_ACCESS_KEY = 'K004XByq9AqVXOrCDoHAsTfv3DiFC3I'


SOCIALACCOUNT_PROVIDERS = {

 "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:

        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
       }
   },
    "github": {

      "SCOPE": [
        "user:email"
     ]
  
      }
  
        }


