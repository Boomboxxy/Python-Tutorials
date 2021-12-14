# kwargs -> kaustubh wankhede arguments -> Just for fun
# kwargs -> keyword arguments -> this is the correct one

# *args
# **kwargs

def func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func(a=1, b=2, c="kaustubh")

data = dict(
    name = "kaustubh",
    age = 19,
    profession = "Instructor",
    address = "123, Street, India, Asia, Earth, Solar System, Milky Way, Universe"
)

func(**data)

