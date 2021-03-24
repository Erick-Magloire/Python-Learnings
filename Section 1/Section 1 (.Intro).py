# This is a sample Python script.

# Press CTRL+ALT+⌘ to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {Erick}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

## Hello World Activity, should print Hello World in the next line
print("Hello World")

## Drawing A Shape Activity
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("\n")
# My Own Indent Line
print("*Story Time*")

## Using Variables and Data Types
# Note: Change from original text, use + sign to separate variables within strings
# There once was a man named *Tom*,
# he was *47* years old.
# He really liked the name *Tom*,
# but didn't like being *47*.
character_name = "Erick"
character_age = "24"
print("There once was a man named " + character_name +", ")
print("he was " +  character_age + " years old.")
# Note: Changing Variable Value within script
character_name = "Jaquizz"
character_age =  "12"
print("He really liked the name " +  character_name +", ")
print("but didn't like being " +  character_age + ".")

## Working With Strings
print("Giraffe\nAcademy")
# Use "\n" to create line breaks

#String Variable
phrase = "Giraffe Academy"
print((phrase) + " is cool") # Example of concatenation or combining variables

phrase = "Giraffe Academy"
print(phrase.islower()) # Comes back as True/False if "phrase" is in lower case

#Length of String - Number of Characters
print(len(phrase))

#Show Value of Specific Position within String, 0 is first position in string
print(phrase[0])
print(phrase[2])

#Using Index Function - Passing a Parameter
print(phrase.index("d"))
#print(phrase.index("z")) # Will Give Back Error if letter is not found in string

#Using the Replace Function
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe","Elephant"))


##Working With Numbers
#Print a Number - use math operations as normal
print(2)
print(2 + (5 - 1) / (3 * 2))

#Modular Operator
print(10 % 3)

#Storing A Number
my_num = -5
print(my_num)

#Absolute Value
print(abs(my_num))

#A number to the nth power (1st number is root, 2nd is to what degree of power)
print(pow(4,2))

#Min and Max - gives largest and smallest number in a set
print(min(5,10))
print(max(5,10))

#Round a number
print(round(17.4))

from math import * #allows for more math functions to be used

#Floor/Ceil Command - Rounds number down(Floor)/up(Ceil)
print(floor(3.7))
print(ceil(3.7))

#Square Root of a number
print(sqrt(36))

##Getting Inputs from Users
#Allow user of code to input value in a variable
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age ".")


