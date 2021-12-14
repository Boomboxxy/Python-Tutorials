import random

print('Welcome to the number geussing game: ')
print('Andres wants some help geussing a number between 1 and 10: ')
number = random.randint(1,10)
i = 0
while i != number:
    i = input('Geuss a number: ')
    i = int(i)
    if i > number:
        print('It\'s High')
    elif i < number:
        print('it\'s Low')
    
print('Your win')