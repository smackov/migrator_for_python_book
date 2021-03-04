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
from environment import set_environ


# The run part
if __name__ == '__main__':
    # Set settings for Django Project
    set_environ()
    # Start article migration
    chapters, sections, articles = lookup_dirs(root_path = settings.PATH_TO_CONTENT)
    print(articles[0].name)
    clear_db()
    populate_db(chapters=chapters, sections=sections, articles=articles)
