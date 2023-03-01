def get_primes(*args):
    for param in args[0]:
        is_Prime = True
        if param == 2:
            yield param
        elif param != 0 and param != 1:
            for nums in range(2, param):
                if param % nums == 0:
                    is_Prime = False
                    break
            if is_Prime:
                yield param


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

