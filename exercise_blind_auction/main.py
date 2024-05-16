from art import logo
print(logo)


print("Welcome to the Blind Auction.")

bids = {}

while True:

    names = input("Type your name: ")
    bid = (input("What's your bid? $"))
    bids[names] = bid
    other_users = input("There are other users who wants to bid?  Y/N  ")


    # Dictionary che prende istruzioni dagli input.
    info_dict = {
        "names": names, 
        "bid": bid,
    }


    if other_users.lower() == "y":
        user_info
        def add_new_items(names, bid, other_users):
            new_entry = {
                "names": names, 
                "bid": bid, 
                "other_users": other_users
            }
        add_new_items(names, bid, other_users)

    else:
        user_info = False
        highest_bidder = max(bids, key=bids.get)
        highest_bid = bids[highest_bidder]
        print(f"THe winner is {highest_bidder} with a bid of ${highest_bid}!")