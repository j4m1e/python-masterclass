"""
Lists - These are mutable i.e. can be changed
"""
list1 = [] # Empty list
print(type(list1)) # Find out what type list1 is
# Define list1 with some values
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
print(len(list1)) # find out the number of elements in a list
# Access elements in a list
print(list1[0]) # first element in the list
print(list1[1]) # second element in the list
print(list1[-1]) # last element in the list
print(list1[-2]) # second to last element in the list
# Replace an element in the list
print(f"Original list: {list1}") # using a f-string to print the list
list1[2] = "HP"
print(f"After the list has been changed: {list1}")
# Max and min values in a list (integer or float)
list2 = [-11, 2, 12]
print(f"New list: {list2}")
print(f"Minimum value in the list: {min(list2)}") # minimum value in the list
print(f"Maximum value in the list: {max(list2)}") # maximum value in the list
# Max and min values of a list (string)
list3 = ["a", "b", "c"]
print(f"New list: {list3}")
print(f"Minimum string in the list: {min(list3)}")
print(f"Maximum string in the list: {max(list3)}")
# Mixed lists cannot use max and min
# Add to list
list1.append(100)
print(f"Adding to 100 to list1 yields: {list1}")
# Remove from list
del list1[4] # remove 10.5 from list using its index
print(f"Removing 10.5 from list1 yields: {list1}")
list1.pop(0) # removes Cisco from the list using its index
print(f"Removing Cisco from list1 yields: {list1}")
list1.remove("Juniper") # remove by specifying the value
print(f"Removing Juniper from list1 yields: {list1}")
# Insert at a particular index in the list
list1.insert(2, "Nortel") # inserts at the 2 index
print(f"Inserting Nortel at index 2 in list1 yields: {list1}")
# Append one list to another 
list2 = [9, 99, 999]
print(f"List1: {list1}")
print(f"List2: {list2}")
list1.extend(list2)
print(f"List1 has been extended with list2 and yields: {list1}")
# Find out the index of an element in the list
print(f"Index of -11 in list1 is: {list1.index(-11)}")
# Find the number of occurances of a certain value in a list
list1.append(10) # add another 10 to list1
print(f"Find out the times that 10 appears in list1: {list1.count(10)}")
# Sorting a list
list2.append(1)
list2.append(25)
list2.append(500)
print(f"Unsorted list2: {list2}")
list2.sort() # sort in ascending order
print(f"Ascending order sort for list2: {list2}") 
list2.reverse() # sort in desending/reverse order
print(f"Decending/reverse order sort for list2: {list2}")
# Using the sorted method which creates a new location in memory for the list
print(f"Ascending order sort for list2: {sorted(list2)}")
print(f"Decending/reverse order sort for list2: {sorted(list2, reverse = True)}")
# Concatinate lists (add together)
print(f"Add list1 and list2: {list1 + list2}")
print(f"Add list2 3 times: {list2 * 3}")
# List slicing - extract various parts of a sequence 
list3 = [1, 2, 3, "a", "b", "c"]
print(f"New list to slice: {list3}")
# slice the first three indexes (0-2). Up to but not including 3
print(f"First 3 indexes in list3: {list3[0:3]}") # list3[:3] could also be used
# slice 3, a & b
print(f"Return 3, a & b: {list3[2:5]}")
# slice from element 3 to the end of the list
print(f"From element 3 to the end of the list: {list3[2:]}")
# whole list using slice
print(f"Whole list using slice: {list3[:]}")
# Negative indexes count from right to left of a list
print(f"Last element in the list: {list3[-1]}")
print(f"Second to last element in the list: {list3[-2]}")
# Extract the slice 3, a & b using negative indexes
print(f"3, a & b using negative indexes: {list3[-4:-1]}")
print(f"Last 3 elements in the list using negative indexes: {list3[-3:]}")
print(f"First 3 elements in the list using negative indexes: {list3[:-3]}")
# Using steps in the slicing process
print(f"Every second element in the list: {list3[::2]}") # every second value
print(f"Using step to reverse the order of the list: {list3[::-1]}") # return the list in reverse order
