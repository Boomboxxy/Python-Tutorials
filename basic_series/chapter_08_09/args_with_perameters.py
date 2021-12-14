# Simple function
def multi(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

numbers = [1,2,3,4,5]
print(multi(*numbers))

# with normal parameters

def mul_nums(num, *args):
    multi = 1
    for i in args:
        multi *= i
    return multi, num

print(mul_nums(1,2,3,4,5))