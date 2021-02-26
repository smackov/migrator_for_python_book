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
    def __init__(self, raw_name, parent_chapter):
        self.raw_name = raw_name
        self.number, self.name = raw_name.split('-', 1) 
        self.parent_chapter = parent_chapter
        
    def __repr__(self):
        return 'Section: "{}"'.format(self.raw_name)
    

class Article:
    """
    Article contains all necessary information for creating itself in db.
    """
    def __init__(self, raw_name, parent_section):
        self.raw_name = raw_name
        self.number, self.name = raw_name.split('-', 1)
        self.parent_section = parent_section 
        
    def __repr__(self):
        return 'Article: "{}"'.format(self.raw_name)
 