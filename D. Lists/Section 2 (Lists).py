###Lists

#How To Create a List (ex: make a list of friends)
friends = ["Kevin", "Karen", "Jim", "John", "Susy"] # [] this signals to Python that a collection of data will be inside those symbols

#How To Access Specific Info in List (Show List)
print(friends)

#Show Result Based on Index (Number Position in Data)
print(friends[0]) #Place Data Set and position in set, remember first place always 0

#Show Result Based on Index from back of lists (add negative sign)
print(friends[-1]) #Going from back of list, first number is -1, not 0

#Show All Results After A Certain Position
print(friends[1:]) #Show all numbers after 2nd position

#Show All Results Within A Certain Range
print(friends[1:3]) #Last Number will not be included in result
#Result will only show Karen & Jim

##Modifying Lists
#Changing index #1 (Karen to new name)
friends[1] = "Foogiano"
print(friends[1])

#-------------------------------

###List Functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "John", "Susy"]

#Extend Function - to combine multiple lists
friends.extend(lucky_numbers) #Be mindful of where you are combining lists
print(friends)

#Add Value to List - *append* adds items to the end of an existing list
friends.append("Locker Room") #added Locker Room added to extended list
print(friends)

#Add Value to List in Specific Position - *insert* (two inputs: the index position to place new value, new value)
friends.insert(2,"Queen Latifah") #New Value in 3rd position, all values after shift 1 position to the right
print(friends)

#Remove Values from a List
friends.remove("Jim")
print(friends)

#Clear a List of all Values
friends.clear()
print(friends)

##Remove only the Last element off a list, pop it off the list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Zeke",  "Jim", "Jim", "John", "Susy"]
friends.pop()
print(friends) #Will Return every item of friends list except Susy

#Find Out if Specific Value in Lists *index*
print(friends.index("Karen")) #Gives Index Position of Value
#Will Return Error Message/Not Show Result if Item is not in the list.

print(friends.count("Jim")) #Counts How Many Values are like the value searched, Jim shows up 2 times

#SortAList - Ascending Order (alphabetacal)
friends.sort()
print(friends)

#Reverse A List
lucky_numbers.reverse()
print(lucky_numbers) #Lucky Numbers List should be backwords

#Create A Copy of A List
friends2 = friends.copy()

print(friends2) #Will Return Same Values in Friends List as new list Friends 2