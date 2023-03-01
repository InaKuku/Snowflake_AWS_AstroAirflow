class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available.get(author):
            library.books_available[author].remove(book_name)
            self.books.append(book_name)
            if not self.username in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for auth, val in library.rented_books.items():
                for book, days in val.items():
                    if book_name == book:
                        return f'The book "{book}" is already rented and will be available in {days} days!'

    def return_book(self, author:str, book_name:str, library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            del library.rented_books[self.username][book_name]
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        self.books.sort()
        return ', '.join(self.books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"




