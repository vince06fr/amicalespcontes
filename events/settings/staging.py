from .base import *

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '10.215.134.87']
INTERNAL_IPS = '127.0.0.1'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
INSTALLED_APPS += [
    #Debug
    'debug_toolbar',
]

MIDDLEWARE += [
    #Debug
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}
