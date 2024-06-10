class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id_value):
        if not isinstance(id_value, int):
            raise ValueError(
                "ID must be of type integer."
            )
        self._id = id_value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_value):
        if not isinstance(title_value, str) and 2 <= len(title_value) <= 100:
            raise ValueError ("Title must be a non-empty string.")
        self._title = title_value

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content_value):
        if not isinstance(content_value, str) and 10 <= len(content_value) <= 1000:
            raise ValueError ("Content must be a non-empty string.")
        self._content = content_value

    @property
    def author_id(self):
        return self._author_id
    
    @author_id.setter
    def author_id(self, author_id_value):
        if not isinstance(author_id_value, int):
            raise ValueError(
                "Author ID must be of type integer."
            )
        self._author_id = author_id_value
    
    @property
    def magazine_id(self):
        return self._magazine_id
    
    @magazine_id.setter
    def magazine_id(self, magazine_id_value):
        if not isinstance(magazine_id_value, int):
            raise ValueError(
                "Magazine ID must be of type integer."
            )
        self._magazine_id = magazine_id_value
