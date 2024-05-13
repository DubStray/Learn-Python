import random
print("Welcome to the Rock - Paper - Scissors game!\n")

rps = ["Rock", "Paper", "Scissors"]
lifes = 3
core_game = True # Variabile Booleana per spegnere/accendere il gioco.

# Si crea un ciclo while con core_game per indicare che il gioco è acceso
while core_game == True:
    while lifes > 0: # Se le vite sono superiori a 0 il gioco continua.
        decisione_giocatore = input("What you choose? Rock, Paper or scissors? ")
        decisione_cpu = rps[random.randint(0, 2)] # Il computer sceglierà randomicamente dalla lista dall'item 0 al 2.
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
    print("You have run out of lifes, game over") # Se le vite scendono a 0 allora verrà printato questo.
    game_restart = input("Wanna play again? Y/N: ").lower() # Da qui partirà il programma per poter restartare il gioco se l'user lo vorrà
    if game_restart.lower() == "y":
        core_game = True
        lifes += 3
        print("\n")
    elif game_restart.lower() == "n":
        core_game = False
        print("See you next time!")
        break
