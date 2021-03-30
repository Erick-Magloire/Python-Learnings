'''
        Tuples
- Tuples are ordered sequences of objects
- They are immutable, their content cannot be changed after creation
'''
## 1. Define a Tuple
# create a new tuple - WITHOUT specifying brackets
new_tuple_one = 1,2,3,4

# print tuple
print(new_tuple_one)

#--------------------------------------------------------
# create a new tuple - with brackets
new_tuple_two = (5,6,"python",8)

# print tuple
print(new_tuple_two)

#--------------------------------------------------------
# create empty tuple
empty_tuple = ()

# check empty tuple
print(empty_tuple)

#--------------------------------------------------------
# create tuple using Constructor
new_tuple_three = tuple(("apple","banana","cherry"))

# check empty tuple
print(new_tuple_three)

#--------------------------------------------------------

# single element tuples
new_tuple_wrong = ("apple") # wrong single element tuple
print(type(new_tuple_wrong))  # outputs string
print(new_tuple_wrong)

new_tuple_right = ("apple",) # correct single element tuple
print(type(new_tuple_right)) # outputs tuple
print(new_tuple_right)

# 2. Indexing in Tuples
'''indexing in tuples works just like strings'''
# define a new tuple
new_tuple = "apple","orange","banana","berry","mango"

print(new_tuple[0]) # zeroth element
print(new_tuple[1]) # first element
print(new_tuple[2]) # second element
print(new_tuple[3]) # third element
print(new_tuple[4]) # fourth element

print(new_tuple[-1]) #last element
print(new_tuple[-2]) #last but one element
print(new_tuple[-3]) #last but two element
print(new_tuple[-4]) #last but three element

try:
    print(new_tuple[5]) # throws error - no fifth element
except IndexError as err:
    print(err)

##3. Tuple Immutability Test
# define tuple
new_tuple = (1,7,'$', 'Summers', 'Winters' )

# try changing tuple content (Cannot change tuples)
try:
    new_tuple[4] = 'Spring' # throws error
except TypeError as err:
    print(err)

##4. Concatenation of Tuples
'''
Tuples are immutable, hence the data stored in a tuple cannot be edited
but it's definitely possible to merge two tuples to create a new tuple
'''
# define two new tuple
new_tuple_one = 9,5,6,4,2,1
new_tuple_two = 'a',5,7,6,3,1
print(new_tuple_one)
print(new_tuple_two)

# add a new element
merged_tuple = new_tuple_one + new_tuple_two

# check merged tuple
print(merged_tuple)

## 5. Multiplication (Duplication) of Tuples
'''duplicates the content of a tuple, the specified number of times'''
# define a tuple
new_tuple = 'a',5,7,6,3,1
print(new_tuple)

# multiply and print result
print(new_tuple*2)
print(new_tuple*3)

# 6. Length of a Tuple
# define a tuple
new_tuple = 'a',5,7,6,3,1
len(new_tuple)

# 7. Min & Max Values of a Tuple
'''
- min() returns the minimum value in the tuple
- max() returns the maximum value in the tuple

both methods accept only tuples having elements of similar data type
'''
# define tuple
new_tuple = 8,12,7,10,52,33,21,99

# check min and max of new_tuple
print(min(new_tuple))
print(max(new_tuple))

# define list
new_tuple = 'x','10','99','twenty','%$','--'

# check min and max of new_list
print(min(new_tuple))
print(max(new_tuple))

## 8. Count of an Element in a Tuple
# define a tuple
new_tuple = 5,3,6,3,1,3,2,3

# count the number of 3s in the tuple
print(new_tuple.count(3))

## 9. Location of the First Occurrence : Indexing within Tuple
# define a tuple
new_tuple = 5,6,3,1,3,2,3

# find the index location of the first occurence of 3
print(new_tuple.index(3))

## 10. Delete a Tuple
'''
You cannot remove the elements in a tuple, but you can delete an entire tuple
'''
# define a tuple
new_tuple = 5,3,6,3,1,3,2,3

# check tuple
print(new_tuple)

# delete the tuple
del(new_tuple)

# check deletion
try:
    print(new_tuple) # will throw an error because tuple doesnt exists
except:
    print(err)