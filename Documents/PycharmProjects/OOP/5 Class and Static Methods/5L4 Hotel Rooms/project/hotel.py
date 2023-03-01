class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        for rm in self.rooms:
            if rm.number == room_number:
                rm.take_room(people)

    def free_room(self, room_number):
        for rm in self.rooms:
            if rm.number == room_number:
                rm.free_room()

    def status(self):
        free_rooms = []
        ocup_rooms = []
        for rm in self.rooms:
            if not rm.is_taken:
                free_rooms.append(rm.number)
            else:
                ocup_rooms.append(rm.number)
            self.guests += rm.guests
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join([str(v) for v in free_rooms])}\nTaken rooms: {', '.join([str(v) for v in ocup_rooms])}"
