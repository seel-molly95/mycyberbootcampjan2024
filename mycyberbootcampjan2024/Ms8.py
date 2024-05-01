# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time
print(time.ctime())

#Start code below this line:
for count in range(1, 6):
    print(count, "mississippi")
    time.sleep(2)
print("ready or not here i come")

print(time.ctime())