import os

from rich import print

from models import Chapter, Section, Article


def run(path):
    """General function."""
    chapters, sections, articles = lookup_dirs(path)
    print(chapters)     
    print(sections)     
    print(articles)     

def lookup_dirs(path):
    """Find all chapters, sections and articles.
    
    Return them as their own classes with properties:
    - raw_names
    - names
    - order_numbers
    - paths (optional)
    """
    # Find all chapters in target path
    chapters = []
    for chapter_name in os.listdir(path):
        chapters.append(Chapter(chapter_name))
    # Find all sections in target path
    sections = []
    for chapter in chapters:
        for section_name in os.listdir(os.path.join(path, chapter.raw_name)):
            sections.append(Section(section_name, chapter))
    # Find all articles in target path
    articles = []
    for section in sections:
        path_to_section = os.path.join(path, section.parent_chapter.raw_name)
        for article_name in os.listdir(path_to_section):
            articles.append(Article(article_name, section.raw_name))
    return chapters, sections, articles

def look_dirs(path):
    # Create walk generator
    walk = os.walk(path)
    
    # Find all chapters in target path.
    # At first time when we calling __next__() func it is in given 'path'
    # working directory
    chapters = [Chapter(name) for name in walk.__next__()[1]] 
    sections = []
    articles = []
    
    # Find all sections and articles in target path
    for path_, dirs, files in walk:
        chapter = get_chapter_folder(path_, chapters)
        if is_chapter_folder():
            
        
        
        # Example: 
        # path_ = '/Users/admin/Developer/Python/Article migrator/content/1-Python basic'
        # path_.rsplit('/', 1) = ['/Users/admin/Developer/Python/Article migrator/content', '1-Python basic']
        # path_.rsplit('/', 1)[1] = '1-Python basic'
        # '1-Python basic' - it's the raw name of parent chapter
        current_chapter_name = path_.rsplit('/', 1)[-1]
        current_chapter = get_chapter(current_chapter_name, chapters)
        for dir_name in dirs:
            if is_section(dir_name):
                sections.append(Section(dir_name, current_chapter))
        for file_name in files:
            if is_article(file_name):
                articles.append(Article(file_name))
                 
                
def is_section(dir_name):
    pass
                
def is_article(dir_name):
    pass

def get_chapter(raw_name, chapters):
    """Get chapter from chapters list by raw_name.
    
    Example:
    >>> chapters = [Chapter: "1-Python basic", Chapter: "2-Python advancing"]
    >>> get_chapter("1-Python basic", chapters)
    Chapter: "1-Python basic"
    """
    for chapter in chapters:
        if chapter.raw_name == raw_name:
            return chapter
    return None

def is_chapter_folder(path, chapters):
    "Check if we in chapter folder -> return True, else False"
    
    """ Get raw_name from path. Example: 
    path_ = '/Users/admin/Developer/Python/Article migrator/content/1-Python basic'
    path_.rsplit('/', 1) = ['/Users/admin/Developer/Python/Article migrator/content', '1-Python basic']"""
    raw_name = path.rsplit('/', 1)[-1]
    
    return get_chapter(raw_name, chapters)
        