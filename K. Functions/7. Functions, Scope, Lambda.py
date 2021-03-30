#---------------

### Functions
'''
functions are reusable pieces of code
they only run when called
they may take input arguments
they may return processed values

def keyword is used at the begeinning of a function to start defining a function

return keyword is used to send some value back after processing
'''
## a. Function Anatomy
# define a function to test for even numbers
  # takes one integer number as an argument
  # and returns true if even and false if not
def is_even(num):
  return num % 2 == 0

# test evenness of 55 by calling the function is_even()
print(is_even(55)) # call function and print output

# test evenness of 100 by calling the function is_even()
print(is_even(100)) # call function and print output

## b. Define function to calculate area of a circle
# input argument is radius

def area_circle(radius):
  ''' # start doc string
  input: radius of circle
  return value: computed value of area
  '''
  area = (22.0/7.0)*radius**2
  return area
print(area_circle(5))

### Scope
'''
  - Scope
a variable is only available from inside the region it is created
  - Local Scope
a variable created inside a function belongs to the local scope of that function
and can only be used inside that function
'''
def myfunc():
  inside_variable = 300 # inside_variable is available only inside myfunc() and not accessible outside
  print(inside_variable)

myfunc() # call the function myfunc()
print(inside_variable) # throws error
however, the local variable can be accessed from a function within the function

def myfunc():

  inside_variable = 300

  def myinnerfunc(): # this is the inner function
    print(inside_variable) # this line accesses the inside_variable value

  myinnerfunc() # call the function myinnerfunc()

myfunc() # call the function myfunc()

print(inside_variable) # but this still throws error

## Global Scope
'''
a variable created in the main body of the Python code is a global variable and belongs to the global scope.
global variables are available from within any scope, global and local
'''
outer_variable = 300

def myfunc():
  print(outer_variable)

myfunc()

print(outer_variable)
'''
"Global" Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
the global keyword makes the variable global.
'''
def myfunc():
  global global_variable
  global_variable = 300
  print(global_variable)

myfunc()

print(global_variable)

#-----------------

### Lambda
'''
is a small anonymous function
can take any number of arguments, but can only have one expression

syntax: lambda arguments : expression
'''
# Lambda function example #1:
plus_ten = lambda x : x + 10
print(plus_ten(5))

# Lambda function example #2:
multiply = lambda a, b : a * b
print(multiply(5, 6))

# Lambda function example #3:
triple_sum = lambda a, b, c : a + b + c
print(triple_sum(5, 6, 3))