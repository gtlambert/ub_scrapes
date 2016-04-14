from .base import *
from .keys import *

DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

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
