"""
Files. 
"""
# Opening & Reading
# open("path&file", "accessmode"). Accessmodes - reading(r), which is the default, writing(w),
# appending(a), binary(b) & exclusive creation(x) - this would mean that it would fail in the file
# already exists
print(f"OPENING & READING FILES")
myFile = open("routers.txt", "r")
# check the access mode that a file has been opened with
print(f"File has been opened with mode: {myFile.mode}")
# access and print out the data in the file
# methods that can be used. 
# read returns the entire contents of the file in the form of a string 
print(f"Use the read method: ")
print(f"{myFile.read()}")
# read only a number of bytes (characters) from the file but remember the cursor concept
# cursor is the position that you are currently located within the file
# because the whole file was read, the position is at the end of the file currently 
# to position the cursor at the beginning of the file, the seek method should be used
# this is using the number of bytes from the beginning of the file, zero will be the
# beginning of the file
# see the current postion of the cursor use the tell method
print(f"The cursor is at the {myFile.tell()} position in the file")
# move the cursor to the beginning of the file
myFile.seek(0)
print(f"The cursor is now at position {myFile.tell()}")
# read just the first 5 characters (bytes) of a file
print(f"The first 5 characters of the file are {myFile.read(5)}")
# readline will return the file content line by line, one line at a time, each time the method
# is called
# go back to the beginning of the file first
myFile.seek(0)
print(f"The first line of the file is {myFile.readline()}")
print(f"The second line of the file is {myFile.readline()}")
# when a blank line is returned, then the end of the file has been reached
# readlines returns a list where each element of list is a line from the file. Very useful for
# iterating over a file & is frequently used when working with strings
# go back to the beginning of the file first
myFile.seek(0)
print(f"Use readlines() to create a list from the lines in the file")
print(f"{myFile.readlines()}")
# use a for loop
# go back to the beginning of the file first
myFile.seek(0)
print(f"Show the routers that start with A")
for line in myFile.readlines():
    if line.startswith("A"):
        # print the line but remove the training newline (\n) by using .rstrip()
        print(f"{line.rstrip()}")
# to create a new file use myFile = open("file&path", "x")
# special care needs to be taken when opening and reading files on windows systems due 
# to the special escape characters in python like \n \t \U, if these are in the path then
# this will throw an exception
# f = open("C:\Users\ted\Desktop\new\test.txt", "r") will through a SyntaxError: (unicode error)
# due to the \U
# therefore an addition escape is required by using an additional backslash
# f = open("C:\\Users\\ted\\Desktop\\new\\test.txt", "r")
# another way to avoid this is error is to do the following which is to use a raw string literal (r)
# this means that all \ in the string is treated as a literal character and not a special escape one
# f = open(r"C:\Users\ted\Desktop\new\test.txt", "r")
print(f"OPENING A FILE FOR WRITING ONLY")
# the w access mode also creates the file for writing if doesn't already exist & overwrites the file
# if it does exist
newFile = open("newfile.txt", "w")
# use the write method to add contents to the file
newFile.write("I like Python!\nDo you?")
# in the interpreter this will return 22 which is the number of characters including new line etc 
# as the file is open writing the read method cannot be used
# if the file is not closed, then the contents will not be written to the file
newFile.close()
# if the file is opened again for writing and new contents written it will overwrite the existing
# use the writeline method to add contents to the file
newFile2 = open("newfile2.txt", "w")
# a tople could also be used newFile2.writelines(("Cisco1", "Juniper2", "HP1"))
newFile2.writelines(["Cisco", "Juniper", "HP"])
newFile2.close()
print(f"APPENDING TO A FILE")
# append adds data to the end of the file if it exists or creates the file if it doesnt exist
newFile3 = open("newfile2.txt", "a")
newFile3.write("this string was appended")
newFile3.close()
# the access modes to allow for the reading of contents immediately after writing are r+, w+ and a+
# use the w+ access mode
newFile4 = open("newfile4.txt", "w+")
newFile4.write("A chunk of text")
# go back to the beginning of the file
newFile4.seek(0)
print(f"Contents from file using the w+ access mode")
print(f"{newFile4.read()}")
newFile4.close()
print(f"CLOSING FILES")
# once a file is opened it is important to close it so that other OS processes can perform actions on it
# a file object attribute can be used to check if a file is closed
print(f"Is newfile4.txt closed: {newFile4.closed}")
# with .. as statement can be used to close a file, this was introducted in Python 2.5. This means that 
# the file does not need to be closed manually using the close method instead the file is closed 
# automatically. With the w access mode it will create a new file too
# the as keyword acts as an assignment operator for the file object (f)
with open("newfile5.txt", "w") as f:
    f.write("Hello Python!")
print(f"Checking that newfile5.txt has been closed: {f.closed}")
print(f"DELETE THE CONTENTS OF A TEXT FILE")
# delete the contents of a text file either completely or partially
# open file for reading & check it is open
file = open("newfile6.txt")
print(f"{file}")
print(f"contents of newfile6.txt")
print(f"{file.read()}")
# to find the length of the file the cursor needs to be reset as the file has been read already
file.seek(0)
print(f"Number of characters in newfile6.txt is {len(file.read())}")
# to delete the contents of a file use the method truncate and the access mode must be write
file.close()
# open the file for reading and writing with the r+ access mode
file = open("newfile6.txt", "r+")
# delete all the contents - this method will return 0 as all characters have been deleted
file.truncate()
print(f"The number of characters in newfile6.txt, after the delete is {len(file.read())}")
file.close()
# add the contents back into the file 
file = open("newfile6.txt", "r+")
file.write("Python is the greatest programming language of all time. Do you agree? :)")
file.seek(0)
print(f"Newfile6.txt is {len(file.read())} characters long and contains the below")
file.seek(0)
print(f"{file.read()}")
file.close()
# delete partially the contents of the file i.e. leave Python is (10 characters)
# open the file for reading and writing with the r+ access mode
file = open("newfile6.txt", "r+")
# leave only 10 characters in the file
file.truncate(10)
file.seek(0)
print(f"Newfile6.txt is {len(file.read())} characters long and contains the below")
file.seek(0)
print(f"{file.read()}")
file.close()

# add the contents back into the file 
file = open("newfile6.txt", "r+")
file.write("Python is the greatest programming language of all time. Do you agree? :)")
file.seek(0)
print(f"Newfile6.txt is {len(file.read())} characters long and contains the below")
file.seek(0)
print(f"{file.read()}")
file.close()