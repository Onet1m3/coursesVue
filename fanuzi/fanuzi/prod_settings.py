import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'sj67567so9Y&%YY%VHJNHUByhjbggvbhUHYG%^&*())()(*yuhnybtr%^&hyvrcr56ghu7yfbgb'

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bazent_db',
        'USER': 'root',
        'PASSWORD': 'admin123',
        'PORT': '3306',
        'HOST': '101.22.1.2',
        # 'OPTIONS': {
        #     "init_command": "SET storage_engine=INNODB; SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;",
        #     'isolation_level': 'read committed',
        # },
    }
}

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
MEDIA_ROOT =  os.path.join(BASE_DIR,'/media/')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'email'
EMAIL_HOST = 'smtp'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# LOGGING = {
#      'version': 1,
#      'disable_existing_loggers': False,
#      'handlers': {
#          'file': {
#              'level': 'DEBUG',
#              'class': 'logging.FileHandler',
#              'filename': os.path.join(BASE_DIR, 'logs/debug.log')
#          },
#      },
#      'loggers': {
#          'django.request': {
#              'handlers': ['file'],
#              'level': 'DEBUG',
#              'propagate': True,
#          },
#      },
#  }