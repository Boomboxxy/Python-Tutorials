def multi(*args):
    total = 1
    for arg in args[0]:
        total *= arg
    return total


def multi2(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 1, 3, 6, 4, 26, 1, 2, 511, 5, 1, 5, 1, 5, 1, 1, 51, 51, 51, 51, 51, 51]

# print(multi(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(multi(numbers))
print(multi2(*numbers))