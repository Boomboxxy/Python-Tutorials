def cube(n):
    three = dict()
    for number in range(1,n+1):
        three[number] = number ** 3
    return three
amount = 3
print(cube(amount))
