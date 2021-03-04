"""
The module for migration articles to db.

Articles is represented as .md files and saved in sorted folders.
"""

import os
import sys

import django

import settings
from lookup_dirs import lookup_dirs
from db import clear_db, populate_db


# The run part
if __name__ == '__main__':
    # Set settings for Django Project
    sys.path.append(settings.PATH_TO_DJANGO_APPS)
    os.environ['DJANGO_SETTINGS_MODULE'] = settings.PATH_TO_DJANGO_PROJECT_SETTINGS
    django.setup()

    # Start article migration
    chapters, sections, articles = lookup_dirs(root_path = settings.PATH_TO_CONTENT)
    print(articles[0].name)
    clear_db()
    populate_db(chapters=chapters, sections=sections, articles=articles)
