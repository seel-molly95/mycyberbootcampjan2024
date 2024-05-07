# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

print("Hello! Let's check out the world wide web together.")
website_address = input("Type the website address you want to visit: ")
if not website_address.startswith('http://') and not website_address.startswith('https://'):
    website_address = 'https://' + website_address
action = input("What do you want to do? Type 'GET' if you want to see something, or 'POST' if you want to share something: ").upper()
print("\nAlright, here's what we're going to do:")
print(f"Action: {action}")
print(f"Website: {website_address}")
confirm = input("\nAre you ready to check it out!? Type 'yes' or 'no': ").lower()
if confirm == "No": 
    print("have a nice day")
if confirm == "yes":
    print("\nLet's dive in to the World Wide Web!")
    print("Getting that information from the world wide web...")
    response = requests.get(website_address)
    print("\nHere's what we found:")
    if response.status_code == 200:
        print("Yay! The website is up and running!")
    elif response.status_code == 404:
        print("Oops! Looks like the website is not found.")
    elif response.status_code == 503:
        print("Sorry, the server is currently unavailable. Please try again later.") 
    elif response.status_code >= 400 and response.status_code < 500:
        print("Oops! There was an error on the clients end.")
    elif response.status_code >= 500 and response.status_code < 600:
        print("Oops! There was an error on the server's end.")   
    else:
        print(f"Hmm... Something went wrong. Error code: {response.status_code}")
else:
    print("\nOkay, maybe next time. Have a great day!")
