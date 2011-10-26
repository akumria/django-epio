# encoding: utf-8
from settings import *
from bundle_config import config

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django_ses.SESBackend'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.getenv('EPIO_DATA_DIRECTORY'), 'media')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config['postgres']['host'],
        "PORT": int(config['postgres']['port']),
        "USER": config['postgres']['username'],
        "PASSWORD": config['postgres']['password'],
        "NAME": config['postgres']['database'],
    },
}
