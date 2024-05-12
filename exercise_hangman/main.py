import random
from hangman_words import word_list
chosen_word = random.choice(word_list) # Variabile per prendere una parola a caso dalla lista.
word_lenght = len(chosen_word) # Variabile che utilizza 'len' per capire quante lettere contiene un parola
lives = 6

from hangman_art import logo
print(logo)

display = []  # Si crea una lista vuota da riempire con i '_' grazie al for loop in range.
for _ in range(word_lenght):
    display += '_'

# Si crea un ciclo While in negativo per far continare il gioco
end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    # Controlla dalla 1 all'ultima lettera per riempirla con quella corretta nel caso l'input fosse giusto.
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    # Utilizzato per chiudere il ciclo.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')

    # Utilizzato per chiudere il ciclo.
    if '_' not in display:
        end_of_game = True
        print('You Win.')

    from hangman_art import stages
    print(stages[lives])  # Le immagini nella lista 'stages' sono [corrisposte] a quelle delle vite.