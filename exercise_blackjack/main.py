import random
from art import logo

def clear():
    print("\n " * 100)




def deal_card():

    '''Distribuisce una carta randomica dal mazzo'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]                                # Lista di "carte" conil relativo modulo che permette
    card = random.choice(cards)                                                         # di scegliere randomicamente dalla lista
    return card



def calculate_score(cards):

    '''Segna lo 0 come Blackjack e fa in modo che l'Ace si possa trasformare in 1 quando c'e' ne' bisogno'''

    if sum(cards) == 21 and len(cards) == 2:                                            # Controllo if sulla somma delle carte e se quella mano ha 2 carte
        return 0                                                                        # ritorna 0 se e' blackjack
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)                                                                # Controllo if per vedere se nelle carte c'e' 11 e se il sum e' superiore
        cards.append(1)                                                                 # a 21, nel caso togliera' 11 e mettera' 1 per non fa sballare
    return sum(cards)



def compare(user_score, computer_score):

    '''Fa una comparison dei risultati con quelli del computer'''

    if user_score > 21 and computer_score > 21:
        return "\nYou went over, you lose!"
    
    if user_score == computer_score:
        return "\nIt's a Draw!"
    elif computer_score == 0:                                                            # Funzione che controlo tutte le possibili casistiche per confrontare
        return "\nBLACKJACK! COMPUTER WINS!"                                               # il risultato dell'utente con quello del computer e controllano se
    elif user_score == 0:                                                                # hanno un blackjack
        return "\nBLACKJACK! YOU WIN!"
    elif user_score > 21:
        return "\nYou went over! You lose!"
    elif computer_score > 21:
        return "\nComputer went over! You win!"
    elif user_score > computer_score:
        return "\nYou win!"
    else:
        return "\nYou lose!"



def play_game():

    print(logo)

    user_cards = []                                                                      # Liste da riempire con le relative carte
    computer_cards = []
    is_game_over = False                                                                 # Boolean per definire la chiusiura del gioco

    for _ in range(2):                                                                   # For loop in range di 2 che deala le carte 2 volte all'user e alla CPU
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)                                         # While loop in negativo per calcolare lo score delel carte
        computer_score = calculate_score(computer_cards)
        
        print(f"    Your cards: {user_cards} = [{user_score}]")                              # Printa i risultati sul display
        print(f"    Computer's first card: [{computer_cards[0]}]")                             # {computer_cards[0]} mostra solo la prima carta a causa delle regole del BJ
        if user_score == 0 or computer_score == 0 or user_score > 21:                    # Controlo if per far stoppare il gioco se CPU o Player hanno il BJ o se il Player
            is_game_over = True                                                          # va oltre il 21
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n to pass: ")
            if user_should_deal == "y":                                                  # Altrimenti il Player puo' decidere se prendere un'altra carta o passare
                print("\n")
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:                                   # Per regole del BJ il banco deve continuare a prendere carte se il ruo risultato
        computer_cards.append(deal_card())                                               # e' minore di 17 (!= significa: not equal)
        computer_score = calculate_score(computer_cards)

    print(f"    You final hand: {user_cards} = [{user_score}]")
    print(f"    Computer's final hand: {computer_cards} = [{computer_score}]")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()                                                                              # While loop per iniziare/continuare/fermare il gioco
    play_game()
