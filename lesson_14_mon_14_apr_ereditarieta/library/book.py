class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.auth = author
        self.isbn = isbn
    
    def describe(self):
        return f"Title: {self.title}, Author: {self.auth}, ISBN: {self.isbn}"