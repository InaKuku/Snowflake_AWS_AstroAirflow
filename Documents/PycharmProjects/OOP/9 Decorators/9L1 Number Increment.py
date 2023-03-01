def number_increment(numbers):


    def increase():
        res = []
        for i in numbers:
            res.append(i+1)
        return res

    return increase()

print(number_increment([1, 2, 3]))