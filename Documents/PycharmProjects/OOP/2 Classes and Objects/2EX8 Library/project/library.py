class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if not user in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            if user.username in self.rented_books:
                del self.rented_books[user]

        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        filt_users = []
        for us in self.user_records:
            if us.user_id == user_id:
                filt_users.append(us.user_id)
                if not us.username == new_username:
                    old_username = us.username
                    us.username = new_username
                    if old_username in self.rented_books:
                        users_books = self.rented_books[old_username]
                        self.rented_books[us.username] = users_books
                        del self.rented_books[old_username]
                    return f"Username successfully changed to: {new_username} for userid: {us.user_id}"
                else:
                    return "Please check again the provided username - it should be different than the username used so far!"
        if len(filt_users) == 0:
            return f"There is no user with id = {user_id}!"
