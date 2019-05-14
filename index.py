import random
from random import randint

player_wins = 0
computer_wins = 0
player2_wins = 0
print('Rock, Paper and Scissors')

player1 = raw_input('Do you want to play with a friend or computer? Type friend or computer to pick')

if player1 == 'friend':
    while player_wins < 5 and player2_wins < 5:
        player1 = raw_input('Player 1, pick your weapon: ')
        player2 = raw_input('Player 2, pick your weapon: ')
        # print(f"player score: {player_wins} computer score: {player2_wins}.") 
        if (player1 == 'rock' and player2 =='scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
            print('Player 1 wins!')
            player_wins += 1
        elif player1 == player2:
            print('It is a tie!')
        elif player1 and player2 != 'rock' or 'paper' or 'scissors':
            print('enter a valid choice!')
        else:
            print("player2 won!")
            player2_wins += 1
    if player_wins > player2_wins:  
        printf("FINAL SCORE: Player Score: {player_wins} player2 score{player2_wins}")
    else: print("Your friend is better, maybe you should play something else!!!")

elif player1 == 'computer':
    print("Score 5 points to win!!!")
    while player_wins < 5 and computer_wins < 5:

        printf("Player Score: {player_wins} computer score{computer_wins}")
        player = input("Player, pick your weapon: ").lower()
        rand_num = randint(0,2)
        if rand_num == 0:
            computer = "rock"
        elif rand_num == 1:
            computer = "paper"
        else:
            computer = "scissors"

        printf("Computer plays {computer}" )

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("player wins!")
                player_wins += 1
            else:
                print("computer wins!")
        elif player == "paper":
            if computer == "rock":
                print("player wins!")
                player_wins += 1
            else:
                 print("computer wins!")
        elif player == "scissors":
            if computer == "paper":
                print("player wins!")
                player_wins += 1
        else:
            print("computer wins!") 
            computer_wins += 1
    else:
        print("Please enter a valid move!")
    if player_wins > computer_wins:  
        printf("FINAL SCORE: Player Score: {player_wins} computer score {computer_wins}")
    else: print("You are bad!!!!")


