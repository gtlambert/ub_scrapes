from .base import *
from .keys import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testing_with_backend',
        'USER': 'postgres',
        'PASSWORD': PASSWORD,
        'HOST': '',
        'PORT': '5433'
    }
}
