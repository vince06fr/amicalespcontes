from .base import *

# Staging settings - unsuitable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS').split(',' )
INTERNAL_IPS = '127.0.0.1'

#Configuration CSRF
CSRF_TRUSTED_ORIGINS = get_env_variable('CSRF_TRUSTED_ORIGINS').split(',' )
# Désactiver la sécurité des cookies pour HTTP
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# Autres configurations de sécurité
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

INSTALLED_APPS += [
    #Debug
    'debug_toolbar',
]

MIDDLEWARE += [
    #Debug
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Databases

# Import DB name, user & password from env variables
DB_NAME = get_env_variable('DB_NAME')
DB_USER = get_env_variable('DB_USER')
DB_PASSWORD = get_env_variable('DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',          # Set to empty string for default.
    }

}

CACHES = {
    'default': {
         'BACKEND':
'django.core.cache.backends.memcached.PyLibMCCache',
         'LOCATION': '/tmp/memcached.sock',
    }
}

# Todo error with logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# ADMINS = ('admin', 'admin@mail.com')
#
# LOGGING = {
# 'version': 1,
# 'disable_existing_loggers': False,
# 'formatters': {
#     'verbose': {
#     'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#     },
#     'simple': {
#     'format': '%(levelname)s %(message)s'
#     },
# },
# 'filters': {
#      'require_debug_false': {
#          '()': 'django.utils.log.RequireDebugFalse'
#      }
#  },
# 'handlers': {
#     # Include the default Django email handler for errors
#     # This is what you'd get without configuring logging at all.
#     'mail_admins': {
#         'class': 'django.utils.log.AdminEmailHandler',
#         'level': 'ERROR',
#         'filters': ['require_debug_false'],
#          # But the emails are plain text by default - HTML is nicer
#         'include_html': True,
#     },
#     # Log to a text file that can be rotated by logrotate
#     'logfile': {
#         'class': 'logging.handlers.WatchedFileHandler',
#         'filename': '../logs/amicalespcontes.log'
#     },
# },
# 'loggers': {
#     # Again, default Django configuration to email unhandled exceptions
#     'django.request': {
#         'handlers': ['mail_admins'],
#                 'level': 'ERROR',
#         'propagate': True,
#     },
#     # Might as well log any errors anywhere else in Django
#     'django': {
#         'handlers': ['logfile'],
#         'level': 'ERROR',
#         'propagate': False,
#         },
#     },
#
# }

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

