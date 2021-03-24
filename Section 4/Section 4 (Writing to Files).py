###Writing to files and appending(adding to) files

''' 3 USES OF WRITING TO FILES
-OVERWRITE FILE
-ADD TO FILE
-CREATE NEW FILES'''

where_the_guys = open("employees.txt", "a") #Change mode to a = append

where_the_guys.write("Gabby - Call of Duty")

where_the_guys.write("\nNew Line") #Adds to end of file in new line

where_the_guys.close() #how to close file after use in code,
                        # ALWAYS DO THIS AFTER FILE USE


#with W, you can create new file by change file name
where_the_guys = open("guys_roster.txt", "w")
#you can also chanhe the format .html/.sql/etc.

#overrides the files and only adds what you want to add
where_the_guys.write("\nAll the bros")

