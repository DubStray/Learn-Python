from art import logo
print(logo)


print("Welcome to the Blind Auction.")

bids = {}                                           # Dizionario vuoto che verrà riempito con le offerte degli utenti.
bidding_finished = False                            # Variabile booleana per far terminare il ciclo.

def clean():
    print("\n " * 90)

def finding_highest_bidder(bidding_record):

    highest_bid = 0                                 # Si creano delle variabili vuote, di testo e numerico da riempire.
    winner = ""

                                                    # Loop che itera tra i NOMI degli users e registra quello che attualmente sta vincendo.
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

                                                    # Un codice che controlla se l'attuale offerta è maggiore rispetto a quella precedente.
                                                    # Se si, procedrà ad aggiornare la variabile highest_bid
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner}, with a bid of ${highest_bid}!")

while not bidding_finished:
    name = input("What's your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    other_users = input("There are other users who wants to bid? Y/N  ").lower()
    if other_users == "n":
        bidding_finished = True
        finding_highest_bidder(bids)
    elif other_users == "y":
        clean()