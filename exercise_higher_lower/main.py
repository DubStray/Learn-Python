import random
from game_data import data
from art import logo, vs

def clear():
    print("\n" * 100)

def choosing_item():                                            # Sceglie una "persona" casuale dal dizionario
    return random.choice(data)

def adjust_item(item):
    name = item("name")                                         # Il compito di questa funzione è quello di ra-
    description = item("description")                           # ccogliere la "persona" casuale presa dal diz-
    country = item("country")                                   # ionario e rendere la frase leggibile prenden-
    return f"{name}, a {description}, from {country}"           # do solo i valori dalle Key



def game():
    print(logo)
    