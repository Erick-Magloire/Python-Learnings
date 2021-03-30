'''Sequence Types''''''
There are three kinds of sequence types:

- lists: mutable sequence
- tuples: immutable sequence
- range: immutable sequence

Other Topics Covered:
- set: an unordered collection of data type that is iterable, mutable and has no duplicate elements.
- dictionaries: dictionary is a collection which is ordered, mutable and does not allow duplicates
- boolean: True or False as a Data type
'''

##'''**Lists**'''## ---Able to be modified---

#1. define a list
''' Syntax: inside this -->  [ ]:  '''
list_example = ['3',92,'x',3.14]
print(dir(list_example))
print(list_example)

print(list_example[1] = 44)
#2. check length of the list
print(len(list_example))

#3. check type of list
type(list_example)

#---------------------------

##'''**Tuples**'''## ---Cannot be modified---
''' Syntax: inside this --> (): '''
#1. define a tuple
tuple_example = (5,'11','a',2.86)
print(dir(tuple_example))
print(tuple_example)

#2. check length of tuple
print(len(tuple_example))

#3. check type
type(tuple_example)

'''
Tuple vs List Comparison

Lists
- ordered group of comma seperated values in square brackets
- square brackets are mandatory
- mutable	
- once created, content changes can be made
- should be chosen if content is not fixed, and keeps changing
- cannot be used as keys for dictionaries	
- are not hashable and immutable	

Tuples
- ordered group of comma seperated values in parenthesis
- parenthesis not mandatory
- immutable
- once created, content cannot be changed
- chosen if content is fixed and never changes
- can be used as keys for dictionaries
- are hashable and immutable
'''

#---------------------------

##'''**Range**'''##
''' Syntax: inside this --> range(int)   '''
#1. define a range
range_example = range(7)
print(range_example)

#2. check length of the range
print(len(range_example))

#3. check type
type(range_example)
''' Syntax: inside this --> ([start], stop, [step]) '''
'''
start: Starting number of the sequence.
stop: Generate numbers up to, but not including this number.
step: Difference between each number in the sequence.
'''
#4. define range with (start,stop,step)
range_example = range(0,20,2)
print(range_example)

#5. check length of the range
print(len(range_example))

#6. check type
type(range_example)

#---------------------------

##'''**Mapping Type - Dictionaries**'''##
''' 
Dictionaries are a mapping data type
- it is mutable
- unordered

Common Methods and Functions for Dictionaries - https://www.tutorialspoint.com/python-mapping-types 
- Method len(d)
    The len() method returns the number of elements in the dictionary.

- Operation d[k]
    It will return the item of d with the key ‘k’. It may raise KeyError if the key is not mapped.

- Method iter(d)
    This method will return an iterator over the keys of dictionary. We can also perform this taks by using iter(d.keys()).

- Method get(key[, default])
    The get() method will return the value from the key. The second argument is optional. If the key is not present, it will return the default value.

- Method items()
    It will return the items using (key, value) pairs format.

- Method keys()
    Return the list of different keys in the dictionary.

-  Method values()
Return the list of different values from the dictionary.

- Method update(elem)
    Modify the element elem in the dictionary.
'''
''' Syntax: inside this -->  {'x':1, 'x2':3, 'x3':5} '''
#1. define a dictionary ( 'Keys': Values )
b = {'one': 1, 'two': 2, 'three': 3}
print(b)

#2. check type
type(b)

#---------------------------

##'''**Set Types**'''##
'''Set is an unordered collection of distinct objects'''
''' Syntax: inside this --> set_variable = {x,x2,x3,x4,x5} '''
set_of_numbers = {0,9,1,5,7}
print(set_of_numbers)
''' Syntax: inside this --> ['x','x2','x3'] '''
names = ('olivia', 'caleb', 'olivia'),('john', 'bill', 'evelyn')
names_set = set(names)
unique_names = list(names_set)
print(unique_names)

#---------------------------

##'''**Boolean Types**'''##
'''state of truth, values may be True or False'''
#1. define a 'true' and 'false' boolean
boolean = True
boolean2 = False

#2. check Boolean value type
type(boolean)
type(boolean2)

#---------------------------


