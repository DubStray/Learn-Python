import random
word_list = ["paper", "rock", "scissors", "bread", "gold", "silver", "human", "monster"]
print("Welcome to the Hangman game!")

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")