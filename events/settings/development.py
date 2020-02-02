from .base import *

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INTERNAL_IPS = '127.0.0.1'

INSTALLED_APPS += [
    #Debug
    'debug_toolbar',
]

MIDDLEWARE += [
    #Debug
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Databases

DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.sqlite3",
       "NAME": os.path.join(PROJECT_ROOT, "../database/db.sqlite3"),
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'amicalespcontes',
#         'USER': 'amicalespcontes',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',          # Set to empty string for default.
#     }
#
# }

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
