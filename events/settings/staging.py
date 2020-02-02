from .base import *

# Staging settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '10.215.134.87']
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

# Import GMAIL user & password from env variables
GMAIL_USER = get_env_variable('GMAIL_USER')
GMAIL_PASSWORD = get_env_variable('GMAIL_PASSWORD')

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = GMAIL_USER
EMAIL_HOST_PASSWORD = GMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Force DDTB
def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}
