def func(name, *args, lastname = "unknown", **kwargs):
    print(name)
    print(args)
    print(lastname)
    print(kwargs)

# PADK

func("kaustubh", 1, 2, 3, x = 1, y= 2, z = 3)
