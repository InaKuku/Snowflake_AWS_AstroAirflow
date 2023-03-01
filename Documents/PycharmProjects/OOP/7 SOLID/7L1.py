# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class ReadingBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

    def turn_page(self, page):
        self.page = page

class Location(Book):
    def __init__(self, title, author, location):
        super().__init__(title, author)
        self.location = location
