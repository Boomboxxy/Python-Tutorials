data = [
    "kaustubh",
    "albert",
    "mark",
    "kaustubh",
    "andres",
    "alan",
]

# .insert() method -> adds the data to the list at index which you provide.
data.insert(-2, "simone")
print(data)

# .extend() method

cars1 = ["BMW i7", "Porsche 346", "Rolls Royce Nx"]
cars2 = ["Camaro", "Tesla Model S", "Nissan Sentra"]

# Created another list to combine 2 lists.
cars = cars1 + cars2
print(cars)

print(cars1)
cars1.extend(cars2)
print(cars1)
