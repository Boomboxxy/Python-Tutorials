# Object Oriented Programming
# class String:
#     def upper():
#         dhjfbjhf
#     pass
# name = "kaustubh"
# print(name.upper())

class Person:
    def __init__(self, first_name, last_name, age, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_no = phone_no

    def introduce_yourself(self):
        return f"My name is {self.first_name} {self.last_name}.\nI am {self.age} years old.\nMy email looks something like this : {self.email}.\nYou can contact me on {self.phone_no}."

person1 = Person(first_name="Kaustubh", last_name="Wankhede", age=14, email="kaustubhwankhede@outlook.com", phone_no="9856320120")
print(person1)
print(person1.first_name)
print(person1.introduce_yourself())