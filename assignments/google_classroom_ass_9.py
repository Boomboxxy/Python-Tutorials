def numbers(*args):
#Will return only the numbers in the arguments
#
    print([i for i in args if type(i) == int or type(i) == float ])

numbers(True, False, [1,2,3], 1, 1.0, 3)
