# It is a ROCK, PLAYER and SCISSORS game where you have to choose one of the three options and computer will also choose one of the three options

import random
print("**** WELCOME TO ROCK, PAPER AND SCISSORS ****\n\n")
print("Enter R for Rock, P for Paper and S for Scissors")
playerscore = 0
computerscore = 0
while True:
    player = input("Enter your choice: ").upper()
    computer = random.choice(['R', 'P', 'S'])
    if (player == "R" and computer == "S") or (player == "S" and computer == "P") or (player == "P" and computer == "R"):
        print("Player score is incremented by 1")
        playerscore+=1
        print("Player: ", playerscore, "Computer: ", computerscore)
        if playerscore == 5 or computerscore == 5:
            print("Game over, Player: ", playerscore, "Computer: ", computerscore)
            exit()
    elif (player == "S" and computer == "R") or (player == "P" and computer == "S") or (player == "R" and computer == "P"):
        print("Computer score is incremented by 1")
        computerscore+=1
        print("Player: ", playerscore, "Computer: ", computerscore)
        if playerscore == 5 or computerscore == 5:
            print("Game over, Player: ", playerscore, "Computer: ", computerscore)
            exit()
    elif player == computer:
        print("Its a tie")
        if playerscore == 5 or computerscore == 5:
            print("Game over, Player: ", playerscore, "Computer: ", computerscore)
            exit()
    else:
        print("Wrong input")