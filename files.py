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