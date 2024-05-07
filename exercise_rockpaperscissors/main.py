import random
print ("Welcome to the Rock - Paper - Scissors game!\n")
rps = ["Rock", "Paper", "Scissors"]
lives = 3
game_is_running = True

while lives > 0:
    decisione_giocatore = input("What you choose? Rock, Paper or scissors? ")
    decisione_cpu = rps[random.randint(0, 2)]
    if decisione_giocatore.lower() == "rock":
        if decisione_cpu == "Rock":
            print("The CPU choose 'Rock', it's a draw!")
            print(f"You have {lives} lives left")
        elif decisione_cpu == "Paper":
            print("The CPU choose 'Paper', you lose!")
            lives -= 1
            print(f"You have {lives} lives left")
        else:
            print("The CPU choose 'Scissors', you win!")
            print(f"You have {lives} lives left")
    if decisione_giocatore.lower() == "paper":
        if decisione_cpu == "Rock":
            print("The CPU choose 'Rock', you win!")
            print(f"You have {lives} lives left")
        elif decisione_cpu == "Paper":
            print("The CPU choose 'Paper', it's a draw!")
            print(f"You have {lives} lives left")
        else:
            print("The CPU choose 'Scissors', you lose!")
            lives -= 1
            print(f"You still have {lives} lives left")
    if decisione_giocatore.lower() == "scissors":
        if decisione_cpu == "Rock":
            print("The CPU choose 'Rock', you lose!")
            lives -= 1
            print(f"You have {lives} lives left")
        elif decisione_cpu == "Paper":
            print("The CPU choose 'Paper', you win!")
            print(f"You have {lives} lives left")
        else:
            print("The CPU choose 'Scissors', it's a draw!")
            print(f"You have {lives} lives left")

if lives == 0:
    print("You have run out of lives, game over.")
    game_is_running = False