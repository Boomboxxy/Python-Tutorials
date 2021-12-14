## COMMON METHOD

def add(a, b):
    return a + b


# print(add(1,2,5,6,7,8,9))  # If we insert more than 2 arguments then python will give an error.


## USING *ARGS

def total(*args):
    total_variable = 0
    for arg in args:
        total_variable = total_variable + arg
    return total_variable


print(total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
