"""
Conditions, loops and exceptions. 
"""
# if / elif / else
# Dont mix spaces and tabs in the code
x = 10
if x > 5:
    print(f"x is greater than 5")
    print(x * 2)
# Multiple cases - can have multiple elif clauses
elif x == 5 and type(x) is int:
    print(f"x is 5 & is an integer")
    print(f"{x}")
elif x == 10 and type(x) is int:
    print(f"x is 10 & is an integer")
    print(f"{x}")
# else is always the last statement & only 1
else:
    print(f"x is not greater than 5")

# for / for-else
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Jumiper"]
for eachVendor in vendors:
    print(f"{eachVendor}")

myString = "Cisco"
for letter in myString:
    print(f"{letter}")
    print(f"{letter * 2}")
    print(f"{letter * 3}")

r = range(10)
for i in r:
    print(f"{i * 2}")
# use range and len to find out the length of the list and then use range as it goes from 0 to up to but not including the last element
for elementIndex in range(len(vendors)):
    print(f"{vendors[elementIndex]}")
# return both the index and the element using enumerate that iterates over the list 
for index, element in enumerate(vendors):
    print(f"{index, element}")
# when the for loop has interated over the entire list, the code below the else statement is executed
for element in vendors:
    print(f"{element}")
else:
    print(f"The end of the list has been reached")

# while / while-else - code will continue to execute until the user defined condition is true
x = 1
while x <= 10:
    print(f"{x}")
    # without the increment below, this while loop would be infinite as this increments x by 1
    x += 1 
else:
    print(f"x is > (greater) than 10")

# nesting - if
x = "Cisco"
# check if i is part of the string x
if "i" in x:
    # checks to see if the string has more than 3 characters 
    if len(x) > 3:
        print(f"The string is {x} and its length is {len(x)}.")
# could be rewritten like this using parethesis to make the code more readable
if ("i" in x) and (len(x) > 3):
    print(f"The string is {x} and its length is {len(x)}.")

# nesting - for. Multiply each element of the 1st list by each element of the 2nd
# iterate over both lists at the same time, do the multiplication and return the result
list1 = [4, 5, 6]
list2 = [10, 20, 30]

# for each element in list1, take each element in list2 and multiply them. Then move onto the next element
# 4 x 10, 4 x 20, 4 x 30, 5 x 10, 5 x 20, 5 x 30, 6 x 10, 6 x 20, 6 x 30
for i in list1:
    print(f"for {i}: ")
    for j in list2:
        print(f"{i * j}")

# nesting - while. Print 5 through 10, 10 times
x = 1
# is x less than or equal to 10
while x <= 10:
    z = 5
    # increment x by 1
    x += 1
    # this while loop gets executed each time the first while loop is executed
    # is z less than or equal to 10
    while z <= 10:
        print(f"{z}")
        # increment z by 1
        z += 1

# nesting - if within a for loop. 
# the for loop interates over the range created by the range function (0 up to 9). 
for number in range(10):
    # greater than or equal to 5 and less than or equal to 9
    if 5 <= number <= 9:
        print(f"{number}")

# Break / continue / pass - control the flow in a while or a for loop. Interrupt or restart the execution
# under certain conditions
# Break - terminate the loop that it resides within
for number in range(10):
    if number == 7:
        break # stop the execution of the loop right here & quit the for loop
    print(f"{number}")
# nested loops
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        if j == 20:
            # inner loop break not outer as well
            break
        print(f"{i * j}")
    print(f"Outside the nested loop")
# Continue - ignore the rest of the code below for the current iteration, goes to the top of the loop and 
# starts the next iteration
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        if j == 20:
            # ignores the rest of the code in the inner loop only for the current iteration
            continue
        print(f"{i * j}")
    print(f"Outside the nested loop")
# Pass - do nothing. If this was missing i.e. pass then an error would be thrown - unexpected EOF while parsing
for i in range(10):
    pass

# Try / except / else / finally - handling exception errors
for i in range(5):
    try:
        # code to check for exceptions
        print(f"{i / 0}")
    # how to handle the exception    
    except ZeroDivisionError as e:
        print(f"{e}, --> division by zero is not allowed.")

# this will throw the standard error as there is no provision for the type of exception that has occurred
"""
for i in range(5):
    try:
        print(f"{i / 0}")
    except NameError:
        print(f"You have a name error in your code")
"""
# when no error occurs
for i in range(5):
    try:
        print(f"{i / 1}")
    except ZeroDivisionError:
        print(f"Division by zero is just wrong")
    print(f"The rest of the code...")
# more comprehensive -  recommended
for i in range(5):
    try:
        print(f"{i / 1}")
    except ZeroDivisionError:
        print(f"Divsion by zero is just wrong")
    except NameError:
        print(f"Name error detected")
    except ValueError:
        print(f"Wrong value")
# else
try:
    print(f"{4 / 2}")
except NameError:
    print(f"Name error!")
else:
    print(f"No exceptions were raised by the try")
# finally
try:
    print(f"{4 / 2}")
except NameError:
    print(f"Name error!")
finally:
    print(f"No exceptions were raised by the try")
