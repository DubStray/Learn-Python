import random

from art import logo
print(logo)

def deal_cards():
    '''Prende una carta qualsiasi dal mazzo'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

for _ in range(2):
    '''Loop per dealare 2 carte sia al'user sia al computer'''
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())


def calculate_score():
    
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    blackjack = 0
    

    for num in user_cards:
        if user_score > 21 and 11 in user_score:
            user_cards.remove(11)
            user_cards.append(1)

    for num in computer_cards:
        if computer_score > 21 and 11 in computer_score:
            computer_cards.remove(11)
            computer_cards.append(1)

    for card in user_cards:
        if 11 in user_cards and 10 in user_cards:
            return 0
        
    for card in computer_cards:
        if 11 in computer_cards and 10 in computer_cards:
            return 0


calculate_score()
