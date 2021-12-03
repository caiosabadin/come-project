from .settings import *

DEBUG = False

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = ''

ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ',
    }
}