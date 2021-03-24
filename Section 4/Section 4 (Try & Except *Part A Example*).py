###Try & Except Commands
##Allows you to address error responses if they come up in your program within the code
'''IN THIS SCENARIO, IF YOU PUT IN AN EQUATION YOU WOULD BE ABLE TO STILL GIVE RESPONSES BUT IF YOU DIVIDE BY 0
THE PROGRAM WILL CRASH.

THIS EXAMPLE SHOWS HOW TO DO MULTIPLE EXCEPT CLAUSES'''
''' Note that that you remove the :
after except when doing multiple exceptions'''



try:
    value = 10 / 0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err) #OR this way prints out what was the error
    print("What???")

except ValueError:
    print ("invalid input")

'''Best practice is to except for specific errors like
ValueError and others:

except: 
        print(sample text)
        
This syntax allows for too board of exceptions'''

#Exception clause allows you to accept certain errors outside of the one specified.
