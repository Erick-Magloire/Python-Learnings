###Try & Except Commands
##Allows you to address error responses if they come up in your program within the code

## When doing 1 exception clause only, use the below syntax
try:
    number = int(input("Enter a number:"))
    print(number)
except:
    print ("invalid input")

#Exception clause allows you to accept certain errors outside of the one specified.

''' PART A EXPLAINS HOW TO DO MULTIPLE EXCEPTIONS'''
''' IN THIS SCENARIO, EVEN IF YOU PUT IN AN EQUATION - IT WOULD GIVE YOU AN INVALID INPUT ERROR SO YOU WOULD WANT TO
SPECIFY WHAT TYPES OF ERRORS COULD COME UP AND HAVE THE PROGRAM CONTINUE RUNNING WITH RESPONSES *SEE PART A*'''



