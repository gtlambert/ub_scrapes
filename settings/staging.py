import os

from base import *

import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
