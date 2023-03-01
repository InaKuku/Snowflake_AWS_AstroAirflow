class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if not album in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for alb in self.albums:
            if alb.name == album_name:
                if not alb.published:
                    self.albums.remove(alb)
                    return f"Album {album_name} has been removed."
                    break
                else:
                    return "Album has been published. It cannot be removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        result = ""
        result += f"Band {self.name}\n"
        for alb in self.albums:
            result += f"{alb.details()}\n"
        return result



