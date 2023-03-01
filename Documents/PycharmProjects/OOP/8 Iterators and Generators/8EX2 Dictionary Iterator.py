class dictionary_iter:
    def __init__(self, dictionary):
        # self.dictionary = [(k, v) for k, v in dictionary.items()]
        self.dictionary = list(dictionary.items())
        self.start_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start_index < len(self.dictionary):
            temp = self.dictionary[self.start_index]
            self.start_index += 1
            return temp
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
