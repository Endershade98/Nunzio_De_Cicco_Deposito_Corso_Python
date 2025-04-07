from datetime import datetime

class Book:
    """Book represents a real book object using its title, author and pages"""
    def __init__(self, title: str, author: str, pages: int, edition: datetime) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.date = datetime
        
    def describe(self) -> str:
        """returns title, author and pages of the book"""
        return f"Book title is: {self.title} \nIt was written by: {self.author} \nhas: {self.pages}"
    
        