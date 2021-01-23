# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
from hangmanlogo import logo, levels
from word_queue import word_queue

print(logo)

chosen_word = random.choice(word_queue)
guess = input("Guess a letter: ").lower()
word_length = len(chosen_word)
lives = 6



#Create blanks
display = []
for _ in range(word_length):
    display += '_'

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've chosen {guess} already, chose another letter")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # Join all the letters onto a list and make it into a string
    print(f"{''.join(display)}")


    if guess not in chosen_word:
        print(f"You guessed the letter {guess} is not in word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")



    #Join all the letters onto a list and make it into a string
    #print(f"{''.join(display)}")


    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(levels[lives])


