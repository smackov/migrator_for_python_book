import os
import re

from rich import print

from models import Chapter, Section, Article


def run(path):
    """General function."""
    chapters, sections, articles = lookup_dirs(path)
    print(chapters)
    print(sections)
    print(articles)


def lookup_dirs(root_path):
    """Find all chapters, sections and articles.

    Return them as lists of their own classes with necessary information.
    """
    # Create empty lists and populate them in next 'for' cycle.
    chapters = []
    sections = []
    articles = []

    # Find all sections and articles in walk generator tree
    for path, dirs, files in os.walk(root_path):
        if we_are_in_root_folder(root_path, path):
            chapters = extract_chapters(dirs)
        if we_are_in_chapter_folder(root_path, path):
            sections += extract_sections(dirs, path, chapters)
        if we_are_in_section_folder(root_path, path):
            articles += extract_articles(files, path, sections)

    return chapters, sections, articles


def we_are_in_root_folder(root_path, current_path):
    if root_path == current_path:
        return True
    return False


def we_are_in_chapter_folder(root_path, current_path):
    path_to_folder, name_of_folder = current_path.rsplit('/', 1)
    if path_to_folder == root_path and is_correct_name(name_of_folder):
        return True
    return False


def we_are_in_section_folder(root_path, current_path):
    path_to_parent_folder, name_of_parent_folder, name_of_folder = current_path.rsplit('/', 2)
    if (path_to_parent_folder == root_path and is_correct_name(name_of_parent_folder)
            and is_correct_name(name_of_folder)):
        return True
    return False


def extract_chapters(dirs):
    return [Chapter(chapter_name) for chapter_name in dirs]


def extract_sections(dirs, current_path, chapters):
    parent_chapter = get_chapter_by_name(current_path.rsplit('/', 1)[-1], chapters)
    return [Section(section_name, parent_chapter) for section_name in dirs]


def extract_articles(files, current_path, sections):
    parent_section = get_section_by_name(current_path.rsplit('/', 1)[-1], sections)
    return [Article(article_name, parent_section) for article_name in files]


def is_correct_name(name):
    """
    Check is the name correct to be a name of chapter, section or article.

    Their names must be look like: '10-File handling', '1-Python basic', '5-Types'."""
    if re.match(r'^[\d]+-[\w\s]+$', name) != None:
        return True
    return False


def get_chapter_by_name(raw_name, chapters):
    """Get Chapter from chapters list by raw_name.

    Example:
    >>> chapters = [Chapter: "1-Python basic", Chapter: "2-Python advancing"]
    >>> get_chapter_by_name("1-Python basic", chapters)
    Chapter: "1-Python basic"
    """
    for chapter in chapters:
        if chapter.raw_name == raw_name:
            return chapter
    return None


def get_section_by_name(raw_name, sections):
    """Get Section from sections list by raw_name.

    Example:
    >>> sections = [Section: "1-File Handling", Section: "2-Data types"]
    >>> get_section_by_name("1-File Handling", sections)
    Section: "1-File Handling"
    """
    for section in sections:
        if section.raw_name == raw_name:
            return section
    return None
