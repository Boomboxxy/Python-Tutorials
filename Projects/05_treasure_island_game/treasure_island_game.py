print('Welcome to treasure island!')

crosswords = input('You reach a crossroad; Should you go left or right?')
i = 0
while i < 1:
    if crosswords == 'right':
        print('You get lost. You lose!')
        break
    elif crosswords == 'left':
        print('Your have reached an Island.')

    island = input('Do you want to wait or swim?')

    if island == 'swim':
        print('Your are attacked by an angry trout. You Lose!')
        break
    elif island == 'wait':
        print('A ferry takes you accross to the island')

    doors = input('Your see three doors in front of you.\n They are red, blue, and yellow. Which do you choose?')

    if doors == 'blue':
        print('You find the room is full of beasts. You Lose!')
        break
    elif doors == 'red':
        print('The room is full of fire. Your Lose!')
        break
    elif doors == 'yellow':
        print('Your found the treasure! Congratulations you Win!!')
        break
