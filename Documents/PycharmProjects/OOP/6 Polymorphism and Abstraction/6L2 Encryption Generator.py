class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other: int):
        new_str = ""
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        else:
            for a_letter in self.text:
                new_numb = ord(a_letter).__add__(other)
                while new_numb < 32:
                    new_numb += 95
                while new_numb > 126:
                    new_numb -= 95
                new_str += chr(new_numb)

        return new_str

example = EncryptionGenerator('Super-Secret Message')
print(example + 20)

