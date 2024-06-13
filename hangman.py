#My Coding Challenge is HANGMAN

#imortrandom is to select a random word from the list i created below

#my function to get a random word is get_random_word(word_list):

#my function for the state of the game is display_game_state(word,guessed_letters, attempts_left),This prints the current state
#of the word, letters guessed, and number of attempts left.

#the main game function is play_hangman(), this is the core game loop that picks a word, prompts the user for a guess, updates the game 
#state based on guesses, and checks the win/loss and show the correct message

#the main function to start the game is main(), this allows the user to play more than once

import random
word_list = ["python", "hangman", "challenge", "programming", "savvy", "ubuntu", "linux", "microsoft", "mac"]
def get_random_word(word_list):
    return random.choice(word_list).upper()
def display_game_state(word, guessed_letters, attempts_left):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {display_word}")
    print(f"Guessed Letters: {' '.join(guessed_letters)}")
    print(f"Attempts Left: {attempts_left}\n")
def play_hangman():
    word = get_random_word(word_list)
    guessed_letters = set()
    attempts_left = 6
    print("Welcome to Hangman!\n")
    while attempts_left > 0:
        display_game_state(word, guessed_letters, attempts_left)      
        guess = input("Enter a letter: ").upper()      
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.\n")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.\n")
            continue
        guessed_letters.add(guess)     
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            attempts_left -= 1
            print(f"Wrong guess. '{guess}' is not in the word.\n")
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word '{word}' correctly!\n")
            return
    print(f"Sorry, you've run out of attempts. The word was '{word}'. Better luck next time!\n")
def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
if __name__ == "__main__":
    main()
