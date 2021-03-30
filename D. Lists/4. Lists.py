'''
        Lists
- Lists are ordered sequences of objects
- They are mutable
'''
# define a list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# view list
print(new_list)

## 1. Accessing List Elements
'''
- indexing in lists works just like strings, indexing starts from zero
'''
# define a list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']


print(new_list[0]) # zeroth element
print(new_list[1]) # first element
print(new_list[2]) # second element
print(new_list[3]) # third element

print(new_list[-1]) # last element
print(new_list[-2]) # last but one element
print(new_list[-3]) # last but two element
print(new_list[-4]) # last but three element

## 2. Nested Lists
'''
- Lists can be embedded inside lists, multiple nesting is also supported
'''
# define nested lists
nested_list = [
               [1,2,3],
               ['a','b','c'],
               [True,False,7],
              ]

# check nested list
print(nested_list)

## 3. List Mutability Test
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# try changing content in list
new_list[2] = 'one' # accepts change

# check list
print(new_list)
## 4. Append to List
''' NOTE: append can add only one element at the end of a list at a time'''
# a. define a list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# b. print new_list
print(new_list)

# c. append 'wohoo' to new_list
new_list.append('wohoo!')

# d. check apended value
print(new_list)

## 5. Extend List
'''used to add multiple elements at the end of the list'''
# a. define a list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# b. print new list
print(new_list)

# c. extend new_list with multiple elements in an array
new_list.extend(["Let's", "do", "this","!"])
# NOTE: multiple elements have to be input in array
print(new_list)

## 6. Insert to List
'''
- Can add an element at a given position in the list
- Can add only one element at a time
    
    *Two arguments* Syntax --->   list.insert( index, value )
1st argument specifies the position
2nd argument specifies the element to be inserted
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# insert element 'Chocolate' at spot 3 in new_list
new_list.insert(3,'Chocolate')

# check insertion
print(new_list)

## 7. Remove from List
'''
- Used to remove an element from the list
- In the case of multiple occurrences, only the first is removed**
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# remove 20 from new_list
new_list.remove(20)

# check removal
print(new_list)

## 8. Pop from List
'''
- Can remove an element from any position in the list, removes value at specified index position
- Element is not specified like in remove() method, only the index position
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# pop spot 2 from list
new_list.pop(2)

# check list
print(new_list)
'''
remove() vs. pop()
A. remove()	
- removes element by identification	
- new_list.remove(element_to_remove)	

B. pop()
- removes by index
- new_list.remove(index_number_to_remove)
'''

## 9. List Slicing
'''
Used to extract a sub-section of the list
index access works like string indexing and slicing
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# extract combinations of new_list extracts
print(new_list[:4])
print(new_list[2:])
print(new_list[1:5])
print(new_list[:])

## 10. Reverse a List
''' 
Used to reverse the elements of a list, can be done in two ways:
- modifying the original list
    OR
- without modifying the original list
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# without modifying the original list
print(new_list[::-1])
print(new_list) # unmodified original list

# modify the original list
new_list.reverse() # modify original list
print(new_list)

## 11. Length of a List
'''returns the number of elements in the list'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# print length of new_list
len(new_list)
Min & Max Values of a List
min() returns the minimum value in the list
max() returns the maximum value in the list

#NOTE: both methods accept only homogeneous lists

## 12. List having elements of similar data type
# define list
new_list = [8,12,7,10,52,33,21,99]

# check min and max of new_list
print(min(new_list))
print(max(new_list))

# define list
new_list = ['x','10','99','twenty','%$','--']

# check min and max of new_list
print(min(new_list))
print(max(new_list))

## 13. Count of an Element in a List
'''returns the number of occurrences of a given element in the list'''
# define list
new_list = [8,12,7,10,7,33,21,7]

# count the number of occurences of 7
print(new_list.count(7))

# count the number of occurences of 10
print(new_list.count(10))

# 14. Concatenate Lists
'''used to merge two lists and return a single list'''
# a. define two lists
list_first = ['three','hundred']
print(list_first)

list_second = ['words','in','a','paragraph']
print(list_second)

# b. concatenate lists
list_combined = list_first + list_second
print(list_combined)

# 15. <ultiply List Content
'''
Allows duplicating the list 'n' amount of times
resultant list is the original list iterated 'n' amount of times
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# multiply list
print(new_list*2)
print(new_list*3)

# 16. Location of the First Occurrence (Indexing within List)
''' 
list.index() method returns the position of the first occurrence of the given element

optional parameters:
- the begin index and
- the end index

when optional arguments are given:
the element is searched only in the sub-list bound by the begin and end indices
when not supplied, the element is searched in the whole list
'''
# define list
new_list = [3,7,20,'@','TECH I.S.', 'makes learning fun!']

# search index of 'TECH I.S.'
print(new_list.index('TECH I.S.'))

# search '@' with optional arguments
print(new_list.index('@',1,4))

## 17. Sort a List in Place
'''
list.sort method sorts the list in ascending order
Can only be performed on lists having elements of similar data type (All numbers, all letters, etc.)
'''
# define list
new_list = [4, 2, 6, 5, 0, 1]

# check unsorted list
print(new_list)

# sort list
new_list.sort()

# check sorted list
print(new_list)

# 18. Create copy of Sorted List
'''
leave the original list unsorted
but create a new list with sorted items
'''
# define list
new_list = [4, 2, 6, 5, 0, 1]

# print sorted list
new_sorted_list = sorted(new_list)

# check original list
print(new_list)

# check sorted list
print(new_sorted_list)

## 19. Erase List Content
'''Erase all content from list'''
# define list
new_list = [4, 2, 6, 5, 0, 1]

# check unsorted list
print(new_list)

# clear list
new_list.clear()

# check cleared list
print(new_list)