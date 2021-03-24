###For Loops, loops through a set of information
#Simple Loop - for x in ______
friends = ["Jim", "Karen","Erick","John Cena"]
len(friends)

for letter in "Giraffe Academy": #for every letter in "Giraffe Academy", something different should be returned back
    print(letter)
# you can name the for variable whatever you want, variable has to be included in the loop
for friend in friends: #for every name in friends list, a different value should be returned back
    print(friend)

##using in "for x in range():" - returns and loops until all variables in range before the one specified
for bo in range(10):
    print(bo)
#returns numbers between first and last integer
for bo in range(4,7):
    print(bo)
##Using length to return value in an array by position
for index in range(len(friends)):
    print(friends[index])

##Using More Complex Logic within For Loops
for index in range(4):
    if index == 0: #when code is ran, when the first number in the range comes up, print "First pass message"
        print("Hol up")
    if index == 3:
        print("3 Bad Bitches")
    else:
        print("okay")

#-------------------

###Exponents

#Raising a number to a power
print(2**3)

#Creating function to raise exponent based on inputs with a For Loop
def raise_to_power(base_num, pow_num):
    result = 1 #Create a variable to be the return value
    for index in range(pow_num): #will execute for loop until power number is reached
        result = result * base_num #Allows for base number to be multiplied again when loop restarts
    return result

print (raise_to_power(2,3))



