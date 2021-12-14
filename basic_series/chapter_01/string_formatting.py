first_name = "Andres"
last_name = "Rodriguez"
age = 21

# Concatenation -> Join strings together

print("Hey! "+first_name+" "+last_name+". We recently got to know that your age is "+str(age)+".")

# .format() method
# {} -> placeholders
print("Hey! {} {}. We recently got to know that your age is {}.".format(first_name, last_name, age))

# f string
print(f"Hey! {first_name} {last_name}. We recently got to know that your age is {age}.")
