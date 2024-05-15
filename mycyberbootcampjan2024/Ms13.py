# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:
import random
def play_game():
    while True:
        print("Let's play the classic  Rock, Paper, Scissors Shoot Game!")
        player_choice = input("Type 'rock', 'paper', or 'scissors': ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose:", computer_choice)
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break  
play_game()
print("Good game, That was fun, Thanks for playing!")