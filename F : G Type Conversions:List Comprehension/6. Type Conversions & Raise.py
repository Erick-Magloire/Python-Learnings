###Type Conversions
##Changing the data type of a variable
# a. convert int ---> float
x = 3 # int
print(x)
print(type(x))

y = float(x) #convert by = float(variable_name)
print(y)
print(type(y))

# b. convert float ---> int
y = 56.213 # float
print(y)
print(type(y))

z = int(y) # convert by = int(variable_name)
print(z)
print(type(z))

# c. convert string ---> int
x = '50' # string
print(x)
print(type(x))

y = int(x) # convert by = int(variable_name)
print(y)
print(type(y))

# d. convert int ---> string
x = 2020
print(x)
print(type(x))

y = str(x) # convert by = str(variable_name)
print(y)
print(type(y))

# e. convert string ---> float
x = '3.14'
print(x)
print(type(x))

y = float(x) # convert by = float(variable_name)
print(y)
print(type(y))

# f. convert float ---> string
x = 37.5
print(x)
print(type(x))

y = str(x) # convert by = str(variable_name)
print(y)
print(type(y))

# g. convert list ---> tuple
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']
print(new_list)
print(type(new_list))

new_tuple = tuple(new_list) # convert by = tuple(list_name)
print(new_tuple)
print(type(new_tuple))
# i. convert tuple ---> list
new_tuple = 4,1,45,92,31,60,84
print(new_tuple)
print(type(new_tuple))

new_list = list(new_tuple) # convert by = list(tuple_name)
print(new_list)
print(type(new_list))

# j. convert list ---> set
# define list
new_list = ["olivia","kaseem","caleb","olivia","owen", "olivia"]
print(new_list)
print(type(new_list))

new_set = set(new_list) # convert by = set(list_name)
print(new_set) # extracts only the unique values
print(type(new_set))

# i. convert set ---> list
new_set = {'kaseem', 'olivia', 'caleb', 'owen'}
print(new_set)
print(type(new_set))

new_list = list(new_set) # convert by = list(set_name)
print(new_list)
print(type(new_list))

#-----------------

### List Comprehension
'''
For loops can be written in a single line in python
using list comprehension
'''
# a. create a new list of powers of 0 to 9
powers = [num**2 for num in range(10)] # a for loop defined with list comprehension
print(powers)

##Generator object
'''
Is not explicitly executed at creation

the formula (expression) for creating values is stored inside the generator

the values are accessed with the next function
'''
# b. create a generator object with powers of 0 to 9
powers = (num**2 for num in range(10))
print(powers)

next(powers) # call the first value in the generator

next(powers) # call the next value in the generator

next(powers) # call the next value in the generator

next(powers) # call the next value in the generator

#-----------------

'''See your If/Else, For, While Statements section for examples'''

## Indentation matters in Python
'''
blocks of code are denoted by indentation
if... ,while... and for... code examples above shows how indentation works
- the codes below if, elif and else are indented
- the code below 'while' is indented
- the code below 'for' is indented
'''

## Nested Indentations:
'''
when while,for and if statements are nested within each other, the code has to be further indented
indentation scheme
'''

## "for" vs. "while" loops
'''
choosing the right loop type makes your code more legible and can also help prevent bugs

everything that can be written with a for loop can be written with a while loop, but while loops can solve some problems that for loops don't address easily

you should usually write for loops when possible; use for loops when

you know the number of iterations you need to do - e.g., 500 trials,
one operation per character in a string, or
an action on every element in a list
if you can describe the problem you're trying to solve in terms of each or every element in an iterable object, aim for a for loop.

benefits of a for loop:

using a for loop when possible will decrease the risk of writing an infinite loop
will generally prevent you from running into errors with incrementing counter variables
'''

#---------------

### Raise() Keyword - generate custom errors
'''
you can geenrate a custom error if an exception occurs
this is done with the raise() keyword
'''
## raise exception example #1
x = -1

if x < 0:
  raise Exception("Sorry, number below zero!")
In [ ]:
## raise exception example #2
# you can choose the specific type of Exception to raise
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed!")
