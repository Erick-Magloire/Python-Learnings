###Return Statements & Functions (Output line 1)
##Tell Python to return information back from a function -
#Example: Create function to cube a number (x^3)
def cube(num):
    #return command signals last line of the function, will automatically indent back into regular code
    return num*num*num #Return tells Python to give back the value of the string indicated to the right of it

result = cube(5)
print(result)

#-----------------
###If Statements & Functions (Output line 2)
#If statements when condition is TRUE executes an action, when FALSE goes to next condition or skips to next function in code
##Create A Boolean Variable
is_male = True

if is_male: #Anything below the if statement will be ran if the condition is true
    print("You are a male.")
#Specify different action when statement is false with *ELSE*
else:
    print("You are a slut.")
#-----------------
##Using the *OR* function in if statements (Output line 3)
is_male = True
is_tall = True

if is_male or is_tall: #if 'either' is_male or is_tall = true, print...
        print("You are either tall or a male or both.")
else: #if either condition is false, print
        print("You are either short or a slut or both.")
#-----------------
##Using the *AND* function in if statements (Output line 4)
is_male = False
is_tall = False

if is_male and is_tall: #if is_male and is_tall = true, print...
        print("You are a tall male.")
else: #if either condition is false, print
        print("You are either a slut, short, or a short slut.")
#-----------------
##Using the *ELSEIF* and *NOT* function in if statements (Output line 5)
is_male = False
is_tall = True

if is_male and is_tall: #if is_male and is_tall = true, print...
        print("You are a tall male.")
elif is_male and not(is_tall): #read as is_male = true and is_tall = false
                #not is basically if the condition is not true, then...
        print("You are a short male.")
elif not(is_male) and is_tall: #read as if is_male = false and is_tall = true
        print("You are a tall slut.")
else: #if either condition is false, print
        print("You are a short slut.")



#-----------------
###If Statements and Comparison Operators
#Create function that returns largest number of a set of parameters
def max_num(num1,num2,num3): #Comparisons returns boolean values
    if num1 >= num2 and num1 >= num3: #Reads as if num1 is greater than num2 & num3, show num1
        return num1
    elif num2 >= num1 and num2 >= num3: #Reads as if num2 is greater than num1 & num3, show num2
        return num2
    else: #if previous conditions are wrong, show show num3
        return num3

print(max_num(4, 700, 30))

#Additional Comparison Operator List
# == : Both values are an exact match
# != : Values do not equal each other

