import random
print("Welcome to the Rock - Paper - Scissors game!\n")

rps = ["Rock", "Paper", "Scissors"]
lifes = 3
core_game = True

while core_game == True:
    while lifes > 0:
        decisione_giocatore = input("What you choose? Rock, Paper or scissors? ")
        decisione_cpu = rps[random.randint(0, 2)]
        if decisione_giocatore.lower() == "rock":
            if decisione_cpu == "Rock":
                print("The CPU choose 'Rock', it's a draw!")
                print(f"You have {lifes} lives left")
            elif decisione_cpu == "Paper":
                print("The CPU choose 'Paper', you lose!")
                lifes -= 1
                print(f"You have {lifes} lives left")
            else:
                print("The CPU choose 'Scissors', you win!")
                print(f"You have {lifes} lives left")
        if decisione_giocatore.lower() == "paper":
            if decisione_cpu == "Rock":
                print("The CPU choose 'Rock', you win!")
                print(f"You have {lifes} lives left")
            elif decisione_cpu == "Paper":
                print("The CPU choose 'Paper', it's a draw!")
                print(f"You have {lifes} lives left")
            else:
                print("The CPU choose 'Scissors', you lose!")
                lifes -= 1
                print(f"You have {lifes} lives left")
        if decisione_giocatore.lower() == "scissors":
            if decisione_cpu == "Rock":
                print("The CPU choose 'Rock', you lose!")
                lifes -= 1
                print(f"You have {lifes} lives left")
            elif decisione_cpu == "Paper":
                print("The CPU choose 'Paper', you win!")
                print(f"You have {lifes} lives left")
            else:
                print("The CPU choose 'Scissors', it's a draw!")
                print(f"You have {lifes} lives left")
    print("You have run out of lifes, game over")
    game_restart = input("Wanna play again? Y/N: ").lower()
    if game_restart.lower() == "y":
        core_game = True
        lifes += 3
        print("\n")
    elif game_restart.lower() == "n":
        core_game = False
        print("See you next time!")
        break
