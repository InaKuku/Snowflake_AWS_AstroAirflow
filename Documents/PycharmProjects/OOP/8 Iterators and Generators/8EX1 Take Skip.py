class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.limit = step*(count - 1)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.start
        while temp <= self.limit:
            self.start += self.step
            return temp
        else:
            raise StopIteration

numbers = take_skip(10, 5)
for number in numbers:
    print(number)