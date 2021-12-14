from art import logo,win,lose,tie
import random

print(logo)

cards = (1,2,3,4,5,6,7,8,9,10,"ace")
play_again = "yes"
running = True

def add(a):
#
# adds the cards together
#
# a = list of cards
#  
    total = 0
    for number in a:
        if number == 'ace':
        #checks if ace should be 11 or 1
            if total > 10:
                ace = 1
                total += 1
            else:
                ace = 11
                total += 11
        else:
            total += number
        if total > 21:
            if ace == 11:
                total -= 10
    return total


def blackjack(a):
#
# Checks for blackjack
#
# a = list of cards
#
    if 10 and 'ace' in a:
        blackjack = True
    else:
        blackjack = False
    return blackjack

def player_gain(a):
#
# Asks if player wants new cards
#
# a = list of player cards
# 
    new_card = True
    cards = (1,2,3,4,5,6,7,8,9,10,"ace")
    gain = input('Do you want another card?')
    while gain == 'yes':
        new = random.choice(cards)
        gain = input('Do you want another card?')
    return new

def computer_gain(a,b):
#
# Checks if the computer needs a new card)
#
# a = list of computer cards
# b = computer total
#
    cards = (1,2,3,4,5,6,7,8,9,10,"ace")
    while b < 17:
        new = random.choice(cards)
        a += new
        if new == ace:
            if b > 10:
                ace = 1
                b += 1
            else:
                ace = 11
                b += 11
        else:
            b += new
        if b > 21:
            if ace == 11:
                b -= 10
    return a



while play_again == "yes":
    player = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    while running == True:
        ### checks if either player has gotten blackjack ###
        if blackjack(player) == True:
            print(win)
            break
        elif blackjack(computer) == True:
            print(lose)
            break
        else:
        #    
        # If no player has gotten black jack
        #   

            #
            # The current cards and totals in play
            #
            player_amount = add(player)
            computer_amount = add(computer)
            print(f'Your cards are {player}\nYour Total is {player_amount}')
            print(f'you see the computer has an {computer[0]}')

            #
            # Adds any new cards along with new totals
            #
            player += player_gain(player)
            player_amount = add(player)
            computer = computer_gain(computer,computer_amount)
            computer_amount = add(computer)
            #
            # Checks who wins
            #
            if player_amount > 21 or computer_amount > player_amount and computer_amount < 21:
                print(lose)
                break
            elif player_amount == computer_amount:
                print(tie)
                break
            else:
                print(win)
                break
    play_again = input('Do you want to play again?')
    








