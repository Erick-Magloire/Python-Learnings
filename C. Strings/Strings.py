'''
        Strings
- Strings are ordered sequence of characters
- Strings are immutable (cannot be modified after being created)
'''

##1. Defining Strings
# a. string defined with single quotes
name_one = 'TECH I.S.'
print(name_one)

# b. string defined with double quotes
name_two = "TECH I.S."
print(name_two)

# c. string defined with triple single quotes
name_three = '''This is a long string and supports 
                multiline statements as well
             '''
print(name_three)

# d. string defined with double quotes inside the single quotes
name_four = 'Hello, "TECH I.S. Student"'
print(name_four)

##2. String Immutability Test
# a. define string
s = "hello"

# b. attempt assigment
s[0] = 'y' #throws error - hence strings are immutable

# c. however, **Rebinding** works
#    reassigning s with 'y' concatenated with 'ello' extracted from s
s = 'y' + s[1:len(s)]
print(s)

##3. String Concatenation (Combination)
first_name = "TECH"
last_name = "I.S."
full_name = first_name + ' ' + last_name
print(full_name)

##4. String Length
# check length of string
name = "TECH I.S."
len(name)

#5. String Indexing
'''in Python,
indexing of sequences starts from 0
string is a text sequence,
so indexing for strings starts from 0
'''
# define a string
s = "abc"

# indexing starts from 0 in Python, 0 = 1st position in sequence
# use square brackets and the index number to access data
print(s[0]) # output: a
print(s[1]) # output: b
print(s[2]) # output: c

print(s[-1]) # output: c
print(s[-2]) # output: b
print(s[-3]) # output: a

print(s[3]) # output: index error

# 6. String Slicing
'''
extract sub-sections of a string
slice strings using format [start:stop:step]
step = 1 by default
you may also omit numbers and use only colons (:)
'''
# define a new string
s = 'abcdefgh'

print(s[3:6])     #output: def
print(s[2:6:1])   #output: cdef (Start, Stop, Step)
print(s[3:6:2])   #output: df (Start, Stop, Step)
print(s[::])      #output: abcdefgh (useful for copying string content into new memory location)
print(s[::-1])    #output: hgfedbca (reverse string command)
print(s[4:1:-2])  #output: ec (Steps down in reverse)