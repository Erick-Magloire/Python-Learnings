###Dictionaries
#Assigning a key value pairs that references a certain definition that can be stored, whenever a key value is triggered in the code - it will output the definition

##Use case for dictionary - Converting month abbreviations (Jan/Feb) to full name
monthConversions = {
    #"Key": "Value" **NOTE:All values in dictionary should be unique.**
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    #**NOTE: Keys can also be numbers.** (ex. 0: "Stuff",)
}
#Retrieve value by key
print(monthConversions["Mar"])
#OR
print(monthConversions.get("Basketball", "ITS NOT HERE BABY")) #.get allows you to return default value if key not located in dictionary or will say "None"
print(monthConversions.get("Basketball"))

#----------------------
###While Loop - allows you run through a certain set of code until a condition is false
#Creating a While Loop with an interger
i = 1 #while condition ("loop guard")
while i <=10: #Loop is adding 1 to i until i is less than or equal to 10
    print(i)
    i = i + 1
    #can be printed as "i += 1" shorthand way of coding a variable + 1 command

print("Done with loop")

















