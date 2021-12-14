import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
