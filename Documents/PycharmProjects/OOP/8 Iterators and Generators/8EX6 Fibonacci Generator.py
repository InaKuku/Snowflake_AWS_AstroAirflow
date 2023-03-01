def fibonacci():
    old = 0
    yield old
    nxt = 1
    yield nxt
    res = nxt + old
    yield res
    res_old = res
    res = nxt + res_old
    yield res
    while True:
        nxt = res_old
        res_old = res
        res = nxt + res_old
        yield res


generator = fibonacci()
for i in range(7):
    print(next(generator))