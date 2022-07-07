#Class Modeling in Python- Books

class Book:

    """Book"""

    def __init__(self, title, author, genre):
        self._title = title
        self._author = author
        self._genre = genre
        self._publishDate = None
        self._pagecount = None
    
    #Get

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def publishDate(self):
        return self._publishDate

    @property
    def pagecount(self):
        return self._pagecount

    #set

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author
    
    @genre.setter
    def genre(self, new_genre):
        self._genre = new_genre

    @publishDate.setter
    def publishDate(self, new_publishDate):
        self._publishDate = new_publishDate

    @pagecount.setter
    def pagecount(self, new_pagecount):
        self._pagecount = new_pagecount
    