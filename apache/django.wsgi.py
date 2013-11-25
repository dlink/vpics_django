#!/usr/bin/python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'vpics.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/data/www/vpics'
if path not in sys.path:
    sys.path.append(path)
