import random
from art import logo

def clean():
    print("\n " * 100)



def deal_cards():

    '''Funzione che deala le carte.'''

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]      # Utilizzando random.choice ed assegnandolo alla
    card = random.choice(cards)                               # lista lascio decidere randomicamente la carta
    return card



def calculate_score(cards):

    '''Funzione con lo scopo di calcolare il risultato delle carte nelle mani dei giocatori.'''

    if sum(cards) == 21 and len(cards) == 2:                   # Controllo if che fa un sum sulla lista delle carte
        return 0                                               # se sono maggiori di 21 e se sono 2, ritorna 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)                                       # Controllo if con lo scopo di capire se nella mano
        cards.append(1)                                        # c'è il blackjack
    return sum(cards)



def compare(user_score, computer_score):

    '''Funzione con lo scopo di comparare il risultato dell'user con quello del computer e vedere se si va oltre il 21'''

    if user_score > 21 and computer_score > 21:
        return "You went over! You lose!"
    
    if user_score == computer_score:
        return "It's a Draw!"
    elif computer_score == 0:
        return "BLACKJACK FOR THE COMPUTER! YOU LOSE!"         # Controlli if per comparare i risultati dell'utente
    elif user_score == 0:                                      # con quelli del Computer.
        return "BLACKJACK FOR YOU! YOU WIN!"
    elif user_score > 21:
        return "You went over! You lose!"
    elif computer_score > 21:
        return "Computer went over! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"



def game_is_running():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())                            # For loop in range che usa deal_cards due volte
        computer_cards.append(deal_cards())                        # e con append aggiungo i risultati alla lista
        

    
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} = {user_score}")
        print(f"Computer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_take_card = input("Type 'y' to get another card, 'n' to pass: ")
            
            if user_take_card == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True


            while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_cards())
                computer_score = calculate_score(computer_cards)

                print(f"Your final hand : {user_cards} = {user_score}")
                print(f"Computer final hand: {computer_cards} = {computer_score}")
                print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? (Y/N)  ") == "y":
    clean()
    game_is_running()
