import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("STAGE") == "DEV"

ALLOWED_HOSTS = list(filter(None, os.getenv("ALLOWED_HOSTS_DEV").split(",")))

CORS_ORIGIN_WHITELIST = list(filter(None, os.getenv("CORS_ORIGIN_WHITELIST_DEV").split(",")))

CRF_TRUSTED_ORIGINS = list(filter(None, os.getenv("CSRF_TRUSTED_ORIGINS_DEV").split(",")))

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PROJECT_APPS = [
    'src.apps.users',
    'src.apps.products',
    'src.apps.categories',
    'src.apps.sections',
]
THIRD_PARTY_APPS = [
    'corsheaders',
    'adminsortable2',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'src.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'src.core.wsgi.application'
ASGI_APPLICATION = 'src.core.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'users-auth-service',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://django_auth_api_redis:6379',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         },
#     },
# }


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
FILE_UPLOAD_STORAGE = os.getenv("FILE_UPLOAD_STORAGE")

if FILE_UPLOAD_STORAGE == "local":
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

if FILE_UPLOAD_STORAGE == "s3":
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_REGION_NAME")
    AWS_S3_SIGNATURE_VERSION = os.getenv("AWS_S3_SIGNATURE_VERSION", "s3v4")

    AWS_DEFAULT_ACL = os.getenv("AWS_DEFAULT_ACL", None)

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly'
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }

AUTH_USER_MODEL = 'users.UserAccount'

#######################################################################
# ENV VARIABLES

JWT_SECRET = os.getenv("JWT_SECRET")

RABBITMQ_HOST=os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT=os.getenv("RABBITMQ_PORT")
RABBITMQ_DEFAULT_USER=os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS=os.getenv("RABBITMQ_DEFAULT_PASS")
USERS_SERVICE_QUEUE=os.getenv("USERS_SERVICE_QUEUE")
ENDPOINT_PREFIX='api/v1'
SERVICE_URL=os.getenv("SERVICE_URL")
