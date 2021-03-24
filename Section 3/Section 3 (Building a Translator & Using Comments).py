###Building a Translator in Python
##Monkey Language
##Turns vowels -> g #Translator returns all vowels as a "g"
#ex. Dog -> Dgg or Lap -> Lgp

#---------------
def translate(phrase):
    output = "" #Set variable for translated phrase
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper(): #if letter upper case and is in vowel string
                output = output + "G"
            else: #if letter lower case and is in vowel string
                output = output + "g"
        else:
            output = output + letter
    return output

print(translate(input("Enter a phrase:"))) #I want to print out the result of the translation function after a user gives input

#------------------
###Notating Comments in 2 Ways

## - can use hashtags (Most Common)

'''
Or with to create a line break.
'''

'''also works within the line of code like this'''
print("This")