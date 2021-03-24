###2D Lists - Creating a list containing other lists
#
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    #This list would have 4 rows and 3 columns - useful for creating a grid in Python
]
#Access element in grid by positioning [row][column]
print(number_grid[0][2]) #([row 1][column 3])

#------------------

###Nested Loops
##Using Nested for loop to parse through a 2D List

#returns each list in number_grid as it is stored - normal for loop
for row in number_grid:
    print(row)

#returns 1 element in number_grid until all elements are listed
for row in number_grid:
    for col in row:
        print(col)
