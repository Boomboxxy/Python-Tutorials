print('Welcome to the number geussing game: ')
print('Andres wants some help geussing a number between 1 and 10: ')

i = 0
while i != 8:
    i = input('Geuss a number: ')
    i = int(i)
    if i > 8:
        print('It\'s High')
    elif i < 8:
        print('it\'s Low')
    
print('Your win')