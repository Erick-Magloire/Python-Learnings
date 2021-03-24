##Basic Calculator: Use these numbers as your input
#Enter a number: 4
#Enter a 2nd number: 6.5

#When Python asks for input, it defaults as strings(text)
num1 = input("Enter a number: ") #Asking for First Number
num2 = input("Enter a 2nd number: ") #Asking for 2nd Number
result = int(num1) + int(num2) #Int looks for a whole number, can only input whole numbers

print(result)
#Will return as combination of two strings instead of the value after addition.
#Returns 46.5 instead of 4 + 6.5

#To make an input a number, see below:

num1 = input("Enter a number: ") #Asking for First Number
num2 = input("Enter a 2nd number: ") #Asking for 2nd Number
result = float(num1) + float(num2) #Float will be able to input decimals

print(result)