# encoding: utf-8
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django_ses.SESBackend'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.getenv('EPIO_DATA_DIRECTORY'), 'media')
