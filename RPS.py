### Rock, Paper, Scissors
### Matt Shen
### 3/31/23
import random

RPS = int(input("PvP(1) or PvE(2) [1 or 2]: "))

if RPS == 1:
    
    print("========== Rock Paper Scissors ==========")
    
    # PvP
    player1 = input("Player 1: ").lower()
    player2 = input("Player 2: ").lower()
    
    if player1 == "rock":
        if player2 == "paper":
            print("Player 2 wins!")
        elif player2 == "rock":
            print("It's a tie!")
        elif player2 == "scissors":
            print("Player 1 wins!")
    
    elif player1 == "paper":
        if player2 == "paper":
            print("It's a tie!")
        elif player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
    
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        elif player2 == "rock":
            print("Player 2 wins!")
        elif player2 == "scissors":
            print("It's a tie!")

elif RPS == 2:

    # PVE
    randomChoice = random.randint(1,3)
    if randomChoice == 1:
        bot = "rock"
    elif randomChoice == 2:
        bot = "paper"
    elif randomChoice == 3:
        bot = "scissors"
    print("The AI has chosen.")

    player = input("Player: ").lower()

    if player == "rock":
        if bot == "paper":
            print("The Player wins!")
        elif bot == "rock":
            print("It's a tie!")
        elif bot == "scissors":
            print("The Player wins!")

    elif player == "paper":
        if bot == "paper":
            print("It's a tie!")
        elif bot == "rock":
            print("The Player wins!")
        elif bot == "scissors":
            print("The Player wins!")

    elif player == "scissors":
        if bot == "paper":
            print("The Player wins!")
        elif bot == "rock":
            print("The Player wins!")
        elif bot == "scissors":
            print("It's a tie!")


