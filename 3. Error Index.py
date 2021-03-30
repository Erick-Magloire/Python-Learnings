'''---SyntaxError---'''
list_example = ('3',92,'x',3.14)
    print(list_example[1] = 44)
          ^
#SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
#Trying to change a tuple is not allowed. You can only change lists

'''---NameError---'''
new_tuple = 5,3,6,3,1,3,2,3
del(new_tuple)
print(new_tuple)
##NameError: name 'new_tuple' is not defined

'''---IndexError---'''
new_tuple = "apple","orange","banana","berry","mango"
print(new_tuple[5]) # throws error - no fifth element
##IndexError: tuple index out of range