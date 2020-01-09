"""
Dictionaries. Unordered set of key value pairs separated by a comma & enclosed by {}. 
Very useful for storing information in a specific format. They are mutable i.e. can be modified. 
Dictionary specific procedures have to be used for doing this as they are not indexed by the position of the
element like lists. They are indexed by key. 

Can use numbers, strings and tuplets but not lists are they are mutable
"""
dict1 = {}
print(f"Dictionary: {dict1}")
print(f"Type: {type(dict1)}")
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
print(f"Dictionary: {dict1}")
# Methods
# Corresponding value to a key
print(f"Vendor: {dict1['Vendor']}")
print(f"IOS: {dict1['IOS']}")
# Add a new key/value pair to the dictionary
dict1["RAM"] = "128"
print(f"Dictionary: {dict1}")
# Modify
dict1["IOS"] = "12.3"
print(f"Dictionary: {dict1}")
# Delete
del dict1["Ports"]
print(f"Dictionary: {dict1}")
# Number of key/value pairs in a dictionary
print(f"Number of key/value pairs in the dictionary: {len(dict1)}")
# Find if key is in the dictionary 
print(f"Is IOS in the dictionary: {'IOS' in dict1}")
print(f"Is IOS2 in the dictionary: {'IOS2' in dict1}")
print(f"Is IOS2 not in the dictionary: {'IOS2' not in dict1}")
# 3 important python methods for dictionaries
# keys - get a list of keys as elements (list data type)
print(f"Keys in the dictionary: {dict1.keys()}")
print(f"Type of keys method: {type(dict1.keys())}")
print(f"Return the list of keys: {list(dict1.keys())}")
# Values - get a list of values as elements (list data type)
print(f"Values in the dictionary: {dict1.values()}")
print(f"Type of the values method: {type(dict1.values())}")
print(f"Return the list of values: {list(dict1.values())}")
# Items - return tuples with each key/value pair (list data type)
print(f"Items in the dictionary: {dict1.items()}")
print(f"Type of the items method: {type(dict1.items())}")
print(f"Return the list of items (tuples): {dict1.items()}")
"""
Python 3.6/3.7 updates for dictionaries
Before 3.6 the order of key/values was not maintained, it is now
"""
mydict = {"L1": "Python", "L2": "Java", "L3": "Javascript","L4": "C++", "L5": "C", "L6": "c#", "L7": "Ruby"}
print(f"Dictionary: {mydict}")
# Conversation between data types
num = 2
f = 2.5
print(f"Type of num: {type(num)}")
print(f"Type of f: {type(f)}")
num2 = str(num) # convert number to a string
print(f"Type of num2: {type(num2)}")
f2 = str(f)
print(f"Type of f2: {type(f2)}")
string = "5"
print(f"Type of string: {type(string)}")
integer = int(string) # convert string to integer
print(f"Type of integer: {type(integer)}")
f3 = float(string) # convert string to float
print(f"Type of f3: {type(f3)}")
num3 = 2
print(f"{num3} has a type of {type(num3)}")
f4 = float(num3) # convert integer to float
print(f"{f4} has a type of {type(f4)}")
f5 = int(f4) # convert float to integer
print(f"{f5} has a type of {type(f5)}")
# Sequences
# Convert a tuple into a list using the list function
tup1 = (1,2,3)
print(f"{tup1} has the type of {type(tup1)}")
list1 = list(tup1)
print(f"{list1} has the type of {type(list1)}")
# Convert a list into a tuple
tup2 = tuple(list1)
print(f"{tup2} has a type of {type(tup2)}")
# Convert a list to a set
set1 = set(list1)
print(f"{set1} has a type of {type(set1)}")
# Convert between different numerical presentations of numbers (dec - base 10, bin - base 2 & hex - base 16)
num = 10
num_bin = bin(num)
print(f"num_bin is {num_bin}")
num_hex = hex(num)
print(f"num_hex is {num_hex}")
bin_to_num = int(num_bin, 2)
print(f"bin_to_num is {bin_to_num}")
hex_to_num = int(num_hex, 16)
print(f"hex_to_num is {hex_to_num}")