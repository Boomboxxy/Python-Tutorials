import random

print('Welcome to the number geussing game: ')
print('Andres wants some help geussing a number between 1 and 10: ')
number = random.randint(1,10)
i = 0
attempt = 5
game = 'yes'
while game == 'yes': 
    while i != number or attempt > 0:
        i = input('Geuss a number: ')
        i = int(i)
        if i > number:
            attempt -= 1
            print('It\'s High')
            print(f'Your have {attempt} attempts remaining')
        elif i < number:
            attempt -= 1
            print('it\'s Low')
            print(f'Your have {attempt} attempts remaining')
        elif i == number:
            break

        if attempt == 0:
            break
        

    if attempt == 0:
        print('Your lose')
    else:    
        print('Your win')
        attempt = 5 - attempt
        print(f'You have used {attempt} amount of attempts.')
    attempt = 5
    number = random.randint(1,10)
    game = input('Would you like to play again?')
    if game == 'no':
        break

