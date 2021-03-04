"""
The DB module for work with DjangoORM.

The goal of the module is provide two tasks:
 1. Delete all Chapters, Sections, Articles.
 2. Populate DB with given chapters, section, articles.
"""


from environment import set_environ
set_environ()

from book.models import Article, Section, Chapter


def clear_db():
    Article.objects.all().delete()
    Section.objects.all().delete()
    Chapter.objects.all().delete()


def populate_db(chapters, sections, articles):
    for chapter in chapters:
        Chapter.objects.create(name=chapter.name, serial_number=chapter.number)
    for section in sections:
        parent_chapter = Chapter.objects.get(name=section.parent_chapter.name)
        Section.objects.create(
            name=section.name,
            serial_number=section.number,
            parent_chapter=parent_chapter)
    for article in articles:
        parent_section = Section.objects.get(name=article.parent_section.name)
        Article.objects.create(
            name=article.name,
            serial_number=1,
            parent_section=parent_section,
            text=article.text,
            content_index=article.index)
