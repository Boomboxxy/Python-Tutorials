data = [
    "kaustubh",
    "albert",
    "mark",
    "kaustubh",
    "andres",
    "alan",
]

# Methods

# .count() method -> It counts the no. of times a particular element occurs in a list.
# count = data.count("kaustubh")
# print(count)

# .sort() method -> It sorts all the elements of the list in an alphabetical or numerical order, permanently.
# If we have a combination of letters and numbers it will just spit out an error.
print(f"Original List : {data}")
data.sort()
print(f"Sorted List : {data}")
print(data)

# Functions

# sorted() function -> It sorts all the elements of the list in an alphabetical or numerical order, temporarily.
# print(sorted(data))
# print(data)