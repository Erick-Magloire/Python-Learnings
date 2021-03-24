###Building A More Advance Calculator
##This Function will also a user to do all basic arithmatic and choose what operation they want

#First, getting input from user (3 Variables: 1st Number, 2nd Number, Operator)
num1 = float(input("Enter 1st number: ")) #Converts user input to number, will give error if not number
operator = (input("What operation do you want to do: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Operation Not Supported")