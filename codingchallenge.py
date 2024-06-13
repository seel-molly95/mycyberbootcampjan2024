#Leap year checker coding challenge
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def main():
    while True:
        user_input = input("Enter a year (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            year = int(user_input)
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")
if __name__ == "__main__":
    main()
#****GAME EXPLINATION****
# is_leap_year(year) is the function
# the main function runs an infinite loop that allows the user to input a year or to type exit
# it validates the user's input to ensure it is a valid integer. If the input is invalid, it prompts the user to enter a valid year.
# if the input is a valid year, it checks whether the year is a leap year and prints the result.
# if the user types 'exit', the program prints a goodbye message and exits the loop.
# the game will keep asking the year until the user types exit

