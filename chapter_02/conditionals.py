age = int(input("Insert your age : "))

"""
if age >= 100:
    print("Not applicable")
elif age <= 1:
    print("Not applicable")
elif age >= 21:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
"""

if 18 <= age <= 100:
    print("You are eligible for voting")
elif 18 > age >= 1:
    print("You are not eligible for voting.")
else:
    print("Not Applicable")
