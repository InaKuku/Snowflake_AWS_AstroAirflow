class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.text) - 1:
            raise StopIteration
        temp = self.text[self.index]
        self.index += 1
        if not temp in self.vowel_list:
            return self.__next__()
        return temp

my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)
