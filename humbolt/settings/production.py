import dj_database_url
import django_heroku

from .base import *

DEBUG = False
ADMINS = (
    ('Cristian Socha', 'ccsocha04@gmail.com'),
)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

django_heroku.settings(locals())