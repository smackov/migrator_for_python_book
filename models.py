"""
Helpfull Chapter, Section, Article classes.
"""


class Chapter:
    """
    Chapter contains all necessary information for creating itself in db.
    """

    def __init__(self, raw_name):
        self.raw_name = raw_name
        self.number, self.name = raw_name.split('-', 1)

    def __repr__(self):
        return 'Chapter: "{}"'.format(self.raw_name)


class Section:
    """
    Section contains all necessary information for creating itself in db.
    """

    def __init__(self, raw_name, parent_chapter, path):
        self.raw_name = raw_name
        self.number, self.name = raw_name.split('-', 1)
        self.parent_chapter = parent_chapter
        self.path = path

    def __repr__(self):
        return 'Section: "{}"'.format(self.raw_name)


class Article:
    """
    Article contains all necessary information for creating itself in db.
    """

    def __init__(self, raw_name, parent_section):
        self.raw_name = raw_name
        self.parent_section = parent_section
        self._text = None
        self._name = None
        self._index = None

    @property
    def text(self):
        if self._text == None:
            self.read_article_and_get_text_name_index()
        return self._text

    @property
    def name(self):
        if self._name == None:
            self.read_article_and_get_text_name_index()
        return self._name

    @property
    def index(self):
        if self._index == None:
            self.read_article_and_get_text_name_index()
        return self._index

    @property
    def path_to_article(self):
        return '/'.join((self.parent_section.path, self.parent_section.raw_name, self.raw_name))

    def read_article_and_get_text_name_index(self):
        self._text = self.retrieve_text_from_file()
        self._name, self._index = self.retrieve_name_and_index_from_text()

    def retrieve_text_from_file(self):
        with open(self.path_to_article, 'r') as file:
            return file.read()

    def retrieve_name_and_index_from_text(self):
        header_lines_of_text = [line for line in self._text.split('\n')
                                if line.startswith('#')]
        name = header_lines_of_text[0].strip('# ')
        index = '\n'.join(header_lines_of_text[1:])
        return name, index

    def __repr__(self):
        return 'Article: "{}"'.format(self.raw_name)
