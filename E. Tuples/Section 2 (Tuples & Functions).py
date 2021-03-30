###Tuples - Types of Data Structures
#Coordinate example of Tuple
coordinates = (12,4) #The Variable + Values make up a Tuple

#PLEASE NOTE: Unlike lists, Tuples cannot be modified or change
try:
    coordinates[0] == 66 #Accessing Values in Tuple
    print(coordinates) '''if you try to assign 66 as the value in the tuple, the error code will be shown in the console but still complete the program'''
except TypeError as err:
    print(err)

# (coordinates[1] = 80) this will give error message since Tuples cannot be changed
#Fixed Data is common to be added in a data base of Tuples

'''
Hashable: meaning its value does not change during its lifetime. This allows Python to create a unique 
hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values.

- Hashable data types: int , float , str , tuple , and NoneType . 

- Unhashable data types: dict , list , and set .
'''
#----------------------

###Functions allow you to store a subset of code that does a specific task into an actionable command, able to applied within other codes
##Allows you to organize your code better in terms of what tasks are being done
#To start a function - use def, tells Python "I want to use this function"
def say_hi(name,age): #():signals that the following code will be in that specific command, the code inside of the function will be indented
    print("Hello new user " + name + " ,you are " + age + ".")
    # <---- name & age are the *PARAMETERS* required to run code
#Call a Function - placing the function name with()
print("Top")
say_hi("","")
print("Bottom")
#**NOTE: Result will print "Top", read and execute code in say_hi, then print "Bottom"**

#Adding Parameters to a Function - information must be given to function in order to complete
say_hi("Mike", "40")
say_hi("Kevin", "17")

#Adding Parameters to a Function - information must be given to function in order to complete
say_hi("Mike", "40")
say_hi("Kevin", "17")

def say_hi2(name,age): #():signals that the following code will be in that specific command, the code inside of the function will be indented
    print("Hello Sexy Guy " + name + " ,you are " + str(age) + ".")
    #If you wanted to allow input of integers into a parameter , the age parameter in the function code number be converted to a string

say_hi2("Austin", 43)
say_hi2("Jhonny", 34)