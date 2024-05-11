import random
word_list = ["paper", "rock", "scissors", "bread", "gold", "silver", "human", "monster"]
display = []
print("Welcome to the Hangman game!")

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

word_lenght = len(chosen_word)
print(f"Pssst, you word is {chosen_word}")

for letter in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(0, len(chosen_word)):
    letter = chosen_word(position)
    if letter == guess:
        display[position] = letter

print('hello wolrd')