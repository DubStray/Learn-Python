import random

def choose_number():
    global randnumber
    randnumber = random.randint(1, 100)   


def play_game():

    is_game_over = False
    
    print("Welcome to the number guessing game!")
    difficulty = input("Choose the difficulty: Easy (10 guesses) or Hard (5 Guesses): ").lower()

    global lives
    
    if difficulty == "easy":
        lives = 10
    if difficulty == "hard":
        lives = 5

    choose_number()

    while not is_game_over:
        
        player_choose = int(input("Try to guess the number from 1 to 100!  Number: "))

        if player_choose > randnumber:
            print("Too high")
            lives -= 1
            print(f"You have {lives} guesses left!")

        elif player_choose < randnumber:
            print("Too low")
            lives -= 1
            print(f"You have {lives} guesses left!")
        else:
            print(f"You win!")
            is_game_over = True

        if lives == 0:
            print("GAME OVER")
            break
        
    replay = input("Do you want to play again? Y/N: ").lower()
        
    if replay == "n":
        is_game_over = True
    else:
        play_game()
        if difficulty == "easy":
            lives = 10
        if difficulty == "hard":
            lives = 5
                

play_game()
