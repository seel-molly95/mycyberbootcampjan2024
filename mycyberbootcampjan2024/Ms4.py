# Objectives
# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run
# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.
# This will not run on windows needs to be mac or linux due to os being bash
import subprocess
import os
#im defining the bash commands as variables with descriptions
commands = [
    ("whoami", "Show the current user:"),
    ("ip a", "Show network interfaces:"),
    ("lshw -short", "Show short hardware information:")
]
#looping through the commands and executing each command 
for command, description in commands:
    print(f"\n{description}") 
#using the f is to format this description
#using the \n is to add a new line before the desription
os.system(command)

#result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
#print(result.stdout)
#subprocess.run(["sudo", "bash", "-c", command])
#i found this subpress answer on this site https://www.datacamp.com/tutorial/python-subprocess
#this is the explination of the code: This code imports the subprocess module, which allows the execution of shell commands from within Python.