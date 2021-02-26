"""
The module for migration articles to db.

Articles is represented as .md files and saved in sorted folders.
"""

from migrator import run


# Configuration
PATH_TO_CONTENT = '/Users/admin/Developer/Python/Article migrator/content'

# The run part
if __name__ == '__main__':
    run(PATH_TO_CONTENT)
    