# Write a program that works out whether if a given number is an 
# odd or even number
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is and odd number")

# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = 365
y = 52
z = 12

days_in_a_year = x
weeks_in_a_year = y
months_in_a_year = z
remaining_years_left = 90

years_left = remaining_years_left - age
days_left = years_left * days_in_a_year 
weeks_left = years_left * weeks_in_a_year
months_left = years_left * months_in_a_year

output_message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left until your 90 years old."
print(output_message)
