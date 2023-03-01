class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range (pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = int(photos_count) // 4
        return cls(pages)
        # if photos_count % 4 == 0:
        #     pages = photos_count / 4
        #     return cls(pages)
        # else:
        #     pages = (photos_count / 4)+1
        #     return cls(pages)
        # rows_with_photos = photos_count // 4
        # pics_last_full_page = photos_count % 4
        # if pics_last_full_page > 0:
        #     for row in range(rows_with_photos + 1):
        #         if not row == rows_with_photos:
        #             for col in range(4):
        #                 mtr_classmethod[row][col] = "[]"
        #         else:
        #             for col in range(pics_last_full_page):
        #                 mtr_classmethod[row][col] = "[]"

    def add_photo(self, label):
        for row in range(self.pages):
            if not len(self.photos[row]) == 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row+1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        result = ""
        for row in range(self.pages):
            result += ("-----------\n")
            if len(self.photos[row]) == 4:
                result += ("[] " "[] " "[] " "[]\n")
            elif 0 < len(self.photos[row]) < 4:
                for col in range(len(self.photos[row])):
                    if not col == len(self.photos[row]) - 1:
                        result += ("[] ")
                    else:
                        result += ("[]\n")
            elif len(self.photos[row]) == 0:
                # if not row == len(self.photos) - 1:
                result += ("\n")
        result += ("-----------")
        return result


