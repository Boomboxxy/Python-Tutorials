# What is a Dictionary :
# Dictionary is an unordered collection of elements in a key:value format.
# Dictionaries are declared using curly brackets.

personal_information = {"first_name": "Kaustubh", "last_name": "Wankhede", "age": 14,
                        "email": "kaustubhkalpeshwankhede@outlook.com",
                        'address': "2, CIDCO, Nashik, Maharashtra, India, Asia, Earth, Space, Solar System, Milky Way "
                                   "Galaxy, Universe, Super Universe"}

personal_information2 = dict(first_name="Andres", last_name="Rodriguez", age=21, email="andres.rodriguez@gmail.com",
                             address="2, Hawlock, USA")

print(type(personal_information))
print(personal_information)
print(personal_information["address"])

user_data = dict(
    name="mad max",
    age="horrible 67",
    email="terriblefreakingmax@mad.com",
    address="mad max bunglow, 123, Street, USA",
)

user_data2 = {
    "first_name": "Kaustubh",
    "last_name": "Wankhede",
    "age": 14,
    "email": "kaustubhkalpeshwankhede@outlook.com",
    'address': "2, CIDCO, Nashik, Maharashtra, India, Asia, Earth, Space, Solar System, Milky Way "
               "Galaxy, Universe, Super Universe"
}

# Add Data
user_data2["movies"] = ["Baby Day's Out", "Toy Story", "Mickey Mouse", "Donald Duck", "Titanic"]

print(user_data2)

# Add more items to a list
user_data2['movies'].append('Transformers')
user_data2['movies'].append('2012')
print(user_data2)

