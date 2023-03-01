class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.start >= 0:
            temp = self.start
            self.start -= 1
            return temp
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")