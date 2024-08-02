import random

from game_data import data
from art import logo, vs

def clear():
    print("\n" * 100)


def generate_random_item():
    '''Prende un item a caso da game_data'''
    return random.choice(data)


def format_data(item):
    '''Rende "leggibile" il formato dell'item preso, quindi tramite le key (name, description, country) prende solo i valori'''
    name = item["name"]
    description = item["description"]
    country = item["country"]
    return f"{name}, a {description}, from {country}"
 

def check_answer(guess, a_followers, b_followers):
    '''un controllo if per comparare la risposta dell'user a quella dell'item scelto casualmente'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)

    score = 0
    game_should_continue = True
    item_A = generate_random_item()                             # Inizia il gioco prendendo due item randomici
    item_B = generate_random_item()

    while game_should_continue:                             
        item_A = item_B                                         # Questa parte di While serve nel caso il player indovini la risposta
        item_B = generate_random_item()                         # in quel caso se la risposta giusta era la B, la B diventerà la A

        while item_A == item_B:                                 # Mentre l'item B diventa l'item A, l'item B viene generato nuovamente
            item_B = generate_random_item()

        print(f"Compare A: {format_data(item_A)}.")             # Formatta i dati di ogni item e chiede di compararli
        print(vs)
        print(f"Against B: {format_data(item_B)}.")

        guess = input("Who has more follower? A or B?  ").lower()
        a_follower_count = item_A["follower_count"]             # Segna (non a schermo) i follower count di ogni item per capire chi dei due
        b_follower_count = item_B["follower_count"]             # ha più follower
        is_correct = check_answer(guess, a_follower_count, b_follower_count)    # Farà un check della risposta tra l'input (guess) e i follower di ognuno (A e B)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"That's wrong: final score: {score}")

game()