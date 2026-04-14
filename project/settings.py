

from pathlib import Path
import os
from dotenv import load_dotenv
from decouple import config

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

EMAIL_USE_LOCALTIME = True
DEFAULT_CHARSET = "utf-8"
EMAIL_ENCODING = "8bit"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# el. pašto adresas iš kurio siųsite
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# slaptažodis

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = "lt"

# TIME_ZONE = 'UTC'
TIME_ZONE = "Europe/Vilnius"

USE_I18N = True

# USE_TZ = True
USE_TZ = False


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# sitie skirti paveiksliukams ant masinu

# cia nurodome kur bus katalogas
MEDIA_ROOT = os.path.join(BASE_DIR, "app/media")

MEDIA_URL = "/media/"  # cia nurodome koks jo pavadinimas

LOGIN_REDIRECT_URL = "/"  # cia kai paspaudi login nukreipiai pagrindini puslapi
LOGOUT_REDIRECT_URL = "/"  # paspaudus ogout nukreipia i pagrindini puslapi

AUTH_USER_MODEL = 'app.CustomUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
