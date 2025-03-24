import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)z668c-4w5)q33@3dy!ou00&n6yg953uylx-+!=#b-ze935_+h'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "yourdomain.com",  ]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'donation',
    'cloudinary',
    'cloudinary_storage',
    'corsheaders',
  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dbd5yj7or',
#     'API_KEY': '556483939213575',
#     'API_SECRET': 'E_uOMpge0MK9PtnQMsDQISXimUw'
# }


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'di2tzvjoe',
    'API_KEY': '146855271251878',
    'API_SECRET': 'V2FVkoLLSMvSdoSOs4gi37fSxjY'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.muxfzpktvcfpgwtuznnl',
        'PASSWORD': 'KEIk2GQoqvolluSf',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '5432'
    }
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  
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

ROOT_URLCONF = 'Blood_Donation.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# simanto66
# 7899