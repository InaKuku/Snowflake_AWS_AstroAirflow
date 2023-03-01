def read_next(*args):
    for seq in args:
        for symb in seq:
            yield symb

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')