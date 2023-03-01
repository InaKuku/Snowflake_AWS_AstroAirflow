from math import ceil

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > len(self.sequence):
            mulptipl = ceil(self.number / len(self.sequence))
            self.sequence = mulptipl * self.sequence
        while self.index < self.number:
            temp = self.sequence[self.index]
            self.index += 1
            return temp
        raise StopIteration



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')