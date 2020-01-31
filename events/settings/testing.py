from .base import *

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INTERNAL_IPS = '127.0.0.1'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
