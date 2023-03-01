class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if not self.published:
            if not song.single:
                if not song in self.songs:
                    self.songs.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."
                else:
                    return "Song is already in the album."
            else:
                return f"Cannot add {song.name}. It's a single"
        else:
            return "Cannot add songs. Album is published."

    def remove_song(self, song_name):
        if not self.published:
            for sng in self.songs:
                if sng.name == song_name:
                    self.songs.remove(sng)
                    return f"Removed song {song_name} from album {self.name}."
                    break
            else:
                return "Song is not in the album."

        else:
            return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        result = ""
        result += f"Album {self.name}\n"
        for sng in self.songs:
            result += f"== {sng.get_info()}\n"
        return result



