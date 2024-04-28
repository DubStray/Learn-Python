import random
print ("Welcome to the Rock - Paper - Scissors game!\n")
rps = ["Rock", "Paper", "Scissors"]
while True:
    decisione_giocatore = input("What you choose? Rock, Paper or scissors? ")
    decisione_cpu = rps[random.randint(0, 2)]
    if decisione_giocatore.lower() == "rock":
        if decisione_cpu == "Rock":
            print("The CPU choose 'Rock', it's a draw!")
        elif decisione_cpu == "Paper":
            print("The CPU choose 'Paper', you lose!")
        else:
            print("The CPU choose 'Scissors', you win!")
    if decisione_giocatore.lower() == "paper":
        if decisione_cpu == "Rock":
            print("The CPU choose 'Rock', you win!")
        elif decisione_cpu == "Paper":
            print("The CPU choose 'Paper', it's a draw!")
        else:
            print("The CPU choose 'Scissors', you lose!")
    if decisione_giocatore.lower() == "scissors":
            if decisione_cpu == "Rock":
                print("The CPU choose 'Rock', you lose!")
            elif decisione_cpu == "Paper":
                print("The CPU choose 'Paper', you win!")
            else:
                print("The CPU choose 'Scissors', it's a draw!")