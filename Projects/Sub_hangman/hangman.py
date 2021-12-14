import random
from hangman_art import stages, logo, win, lose
from hangman_words import word_list

print(logo)
play_again = 'yes'

while play_again == 'yes':
    #generates the word you have to geuss
    geuss = random.choice(word_list)
    geuss_len = len(geuss)


    #creates the blanks for hangman
    blanks = []
    for i in range(1,geuss_len + 1):
        blanks.append('_')
    i = 0
    lives = len(stages) - 1

    while i < 7:
        print(stages[lives])
        print(*blanks, sep ='  ')
        your_geuss = input('Geuss a letter!  ')

        ## Checks for all instances of your geuss in the word
        if your_geuss not in geuss:
            print(f'{your_geuss} is not there.')
            i += 1
            lives -= 1
        else:
            ## finds the exact position of the geuss in the word
            correct = [pos for pos, char in enumerate(geuss) if char == your_geuss]

            v = 0
            ##replaces all blanks with the correct geuss you just did
            for element in correct:
                correct_pos = correct[v]
                blanks[correct_pos] = your_geuss
                v += 1

        ## determines when you win or lose
        if '_' not in blanks:
            print(win)
            break
        elif lives == 0:
            print(stages[lives])
            print(f'The word was {geuss}.')
            print(lose)
            break

    #determines if you play again
    play_again = input('Would you like to play again?')
    if play_again == 'no':
        break

