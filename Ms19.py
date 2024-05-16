# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
person_selected = random.choice(names)

response = input(person_selected + ", will you pay for the food today? (yes/no): ")

if response.lower() == "yes":
    print("The bill is on " + person_selected + " today!")
elif response.lower() == "no":
    names.remove(person_selected)  

   
    new_chosen_name = random.choice(names)
    
    print("The bill is on " + new_chosen_name + " today!")
else:
    print("Please enter either 'yes' or 'no'.")
    
    new_chosen_name = random.choice(names)
    print("the bill is on " + new_chosen_name + " today!")
    
