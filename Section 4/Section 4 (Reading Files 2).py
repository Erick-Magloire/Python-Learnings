###Reading files from another document
##Reading text from hmtl/csv/doc/text
##Open File in read mode
'''open("file name", "mode to open in"
"r" = read mode: Just read the information in the file
"w" = write mode: allows you to edit/change content in the file
"a" = append mode: allows you to add info to file, add only
"r+" = read & write mode: allows reading of and writing in file '''

#Read Mode - create a variable to store your read result
where_the_guys = open("employees.txt", "r")
#For Loop, reads out content until no content left
for guys in where_the_guys.readlines():
    print(guys)
try:
    print(where_the_guys.readlines()[0]) #reads file and returns index in file - example: 2nd result read back
except IndexError as err:
    print(err)
where_the_guys.close()