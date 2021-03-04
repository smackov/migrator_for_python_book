"""
The module for migration articles to db.

Articles is represented as .md files and saved in sorted folders.
"""

import settings
from migrator import run

# The run part
if __name__ == '__main__':
    run(root_path=settings.PATH_TO_CONTENT)
    