# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?
import random
def number_guessing_game():
    for _ in range(3): 
        secret_number = random.randint(1, 20)
        guess = None
        num_guesses = 0
        correct_guess = False 
        while guess != secret_number:
            try:
                guess = int(input("Guess the number between 1 and 20: "))
                num_guesses += 1
                if guess < secret_number:
                    print("HIGHER")
                elif guess > secret_number:
                    print("LOWER")
                else:
                    print("Congratulations! You guessed the number", secret_number, "in", num_guesses, "guesses.")
                    correct_guess = True
                    break  
            except ValueError:
                print("Please enter a valid number.")
        if correct_guess:
            break
    else:
        print("Out of turns! The correct number was", secret_number)
number_guessing_game()