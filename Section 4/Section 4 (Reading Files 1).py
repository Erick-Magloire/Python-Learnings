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

print(where_the_guys.readable()) #Checks if file is readable
print(where_the_guys.readline()) #Reads first line in file
print(where_the_guys.readline()) #the command back to back will return the next line after the previous line that was read
print(where_the_guys.read()) #Will return all info in file


where_the_guys.close() #how to close file after use in code,
                        # ALWAYS DO THIS AFTER FILE USE

where_the_guys = open("employees.txt", "r")

print(where_the_guys.readlines()) #Returns contents of file back as a list

where_the_guys.close()
