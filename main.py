"""
The module for migration articles to db.

Articles is represented as .md files and saved in sorted folders.
"""

import os
import sys

import django

import settings
import db
from lookup_dirs import lookup_dirs


# The run part
if __name__ == '__main__':
    chapters, sections, articles = lookup_dirs(root_path = settings.PATH_TO_CONTENT)
    db.clear_db()
    db.populate_db(chapters=chapters, sections=sections, articles=articles)
