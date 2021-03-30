##Operators
#popular kinds of operators
'''
1.numeric operators
2.comparison operators
3.logical operators
4.assignment operators
5.identity operators
6.membership operators
7.bitwise operators
'''

##Numeric Operators
'''used with numeric data types to perform mathematical operations'''
'''
+: addition
-: subtraction
*: multiplication
/: division
//: floor division
%: modulus (remainder)
**: raising to power
abs(): absolute value of number
round(): rounds a number
bin(): get binary version of a number
hex(): get hexadecimal version of a number
'''

# set values of x, y and z for numeric operators exploration
#(run this cell to initialize values for the next few cells!)
x = 5   # integer value
y = 2.75 # float value, with decimal
z = -45 # negative integer

# sum of x and y
print(x + y)

# difference of x and y
print(x - y)

# product of x and y
print(x * y)

# quotient of x and y
print(x / y)

# floored quotient of x and y
print(x // y)

# remainder of x / y
print(x % y)

# absolute value
print(abs(z))

# x raised to power y
print(x ** y)

# rounding a decimal example - round down
print(round(2.1))

# rounding a decimal example - round up
print(round(3.7))

# binary version of the number
print(bin(37))

# hexadecimal version of the number
print(hex(37))

#-------------------------------

##Comparison Operators
'''
Used to compare two values
( < ) less than
( > ) greater than
( <= ) less than or equal to
( >= ) greater than or equal to
( == ) equality, is equal to
( != )  inequality, is not equal to
'''

# Greater Than
i = 3
j = 7
print(i > j)

# Greater Than or Equal
i = 3
j = 7
print(i >= j)

# Less Than
i = 3
j = 7
print(i < j)

# Less Than or Equal
i = 3
j = 7
print(i <= j)

# Equality Test #1
i = 3
j = 7
print(i == j)

# Equality Test #2
i = 3
j = 3
print(i == j)

# Inequality Test #1
i = 3
j = 7
print(i != j)

# Inequality Test #2
i = 3
j = 3
print(i != j)

#-------------------------------

##Logic Operators
'''
used to combine conditional statements
1. and
2. or
3. not
'''
#1. 'not' operator
a = True
print(not a)

'''Logic Tables'''
# a. 'and' Operator
# a and b are true
a = True
b = True
print(a and b)

# b. only a is true
a = True
b = False
print(a and b)

# c. only b is true
a = False
b = True
print(a and b)

# d. a and b are both false
a = False
b = False
print(a and b)

#2. 'or' Operator

# a. a and b are true
a = True
b = True
print(a or b)

# b. only a is true
a = True
b = False
print(a or b)

# c. only b is true
a = False
b = True
print(a or b)

# d. a and b are both false
a = False
b = False
print(a or b)

#-------------------------------

##Assignment Operators
''' 
( = )   |   used to assign values to variables   
Example: a = b (the value of a is now the value of b)

- following operators combine numerical operations at the same time as assignment

( += )  |   Add and Assign: Add right side with left side operand and then assign as new value of 'a'
Example:   a += b
( -= )  |   Subtract AND: Subtract right operand from left operand and then assign as new value, 'True' if both values are equal	
Example:   a -= b
( *= )  |   Multiply AND: Multiply right operand with left operand and then assign as new value of 'a'
Example:   a *= b
( /= )  |   Divide AND: Divide left operand with right operand and then assign as new value of 'a'
Example:   a /= b
( //= ) |   Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to 'a'
Example:   a //= b
( %= )  |   Modulus AND: Takes modulus using left and right operands and assign result to 'a'
Example:   a %= b
( **= ) |   Exponent AND: Calculate exponent(raise power) value using operands and assign as new value of 'a'
Example:   a **= b
'''

# Assignment Operator
x = 21
print(x)

# += operator
x += 3
print(x)

# -= operator
x -= 3
print(x)

# *= operator
x *= 3
print(x)

# /= operator
x /= 3
print(x)

# //= operator
x //= 3
print(x)

# %= operator
x %= 3
print(x)

#-------------------------------
##Identity Operators
#We use identity operators to compare the memory location of two objects.
x = 2
y = "2"

#1. 'is'
print(x is y)

#2. 'is not'
print(x is not y)

#-------------------------------
##Identity Operators
#-------------------------------
###Bitwise Operators
#Act on operands as if they were strings of binary digits. They operate bit by bit, hence the name
x = 10 ## 0000 1010 in binary
y = 4 ## 0000 0100 in binary

'''&	|| Bitwise AND ||example: '''
x & y   # = 0 (0000 0000)
'''|	|| Bitwise OR  || example: '''
x | y   # = 14 #(0000 1110)
'''~	|| Bitwise NOT || example: '''
~x      # = -11 #(1111 0101)
'''^	|| Bitwise XOR || example: '''
x ^ y   # = 14 #(0000 1110)
'''>>	|| Bitwise right shift || example: '''
x >> 2  # = 2 #(0000 0010)
'''<<	|| Bitwise left shift || example: '''
x << 2  # = 40 #(0010 1000)

