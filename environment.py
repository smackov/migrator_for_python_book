import os
import sys

import django

import settings

def set_environ():
    # Set settings for Django Project
    sys.path.append(settings.PATH_TO_DJANGO_APPS)
    os.environ['DJANGO_SETTINGS_MODULE'] = settings.PATH_TO_DJANGO_PROJECT_SETTINGS
    django.setup()
    