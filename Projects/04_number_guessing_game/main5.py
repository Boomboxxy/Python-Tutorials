from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print('Welcome to the number guessing game!')
print('Andres wants some help guessing a number between 1 and 100')




number = randint(1,100)
i = 0
game = 'yes'
while game == 'yes':
    difficulty = input('Choose a difficulty: Type easy or hard: ')
    if difficulty == 'easy':
        attempt = EASY_LEVEL_TURNS
        original = EASY_LEVEL_TURNS
    elif difficulty ==  'hard':
        attempt = HARD_LEVEL_TURNS
        original = HARD_LEVEL_TURNS
    print(f'Your have {attempt} attempts remaining')     
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
        attempt = original - attempt
        print(f'You have used {attempt} amount of attempts.')
    attempt = 5
    number = randint(1,100)
    game = input('Would you like to play again?')
    if game == 'no':
        break
