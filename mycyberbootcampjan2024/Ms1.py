# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
#print()"my name is molly"
#print()"my favorite food is pasta"
#print()"my dream job is anything cyber"

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
a = bool(True)
b =float(3.5)
c = "hello world"
d =int(7)
e =a

# print the length of your string.
#print=(len(c))
#print (e)

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
#savvy = "learning python is awesome!"

# Replace "Awesome" with "great" in the string
#a = savvy.replace ("awesome", "great")
#print (a) 

# Create and assign 3 more variables called name, age and length using the multi-variable naming method.
name, age, length = "molly", "28", "5'6"

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."
minibio = f"Hi my name is {name}, I am {length} and {age} old today."
print (minibio) 
# Create a list of at least 5 elements of mixed data types
List1 = ["hi", 5, .6, "time", name]
print (List1)

# replace a part of it with something else
List1[0] = "bye"
print (List1)
# append or insert several more items to the list
List1.append(age)
# find and print the length of the list
print (len(List1))
# slice a sub-section of the 1st list, and save it to a different 2nd list
List2 = List1[0:2]
# print the 2nd list
print (List2)
# extend your original list with the 2nd list sliced above
List1.append(List2)
print(List1)
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simlist = [1,0,9,4,5]
# sort "simList", and print the list
simlist.sort()
# copy the "simList" list to another 3rd list
List3 = simlist.copy()
print(13)
# add the 2nd and 3rd lists together into a 4th list
List4 = simlist + List3
print (List4)