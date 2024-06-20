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

    if sum(cards) == 21 and len(cards) == 2:
        return 0                                                                        # 
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)



def compare(user_score, computer_score):

    '''Fa una comparison dei risultati con quelli del computer'''

    if user_score > 21 and computer_score > 21:
        return "You went over, you lose!"
    
    if user_score == computer_score:
        return "It's a Draw!"
    elif computer_score == 0:
        return "BLACKJACK! COMPUTER WINS!"
    elif user_score == 0:
        return "BLACKJACK! YOU WIN!"
    elif user_score > 21:
        return "You went over! You lose!"
    elif computer_score > 21:
        return "Computer went over! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"



def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards} = [{user_score}]")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"You final hand: {user_cards} = [{user_score}]")
    print(f"Computer's final hand: {computer_cards} = [{computer_score}]")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
