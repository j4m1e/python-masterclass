"""
Tuples. Immutable lists i.e. contents cannot be changed. These are ordered so indexes and duplicates are allowed. 
tuples vs lists
fixed length vs variable length
tuples ()
lists []
tuples - immutable
tuples - mutable

"""
my_tuple = ()
print(f"Type is : {type(my_tuple)}")
# Single element in a tuple needs a trick; a trailing comma
my_tuple = (9)
print(f"Contents: {my_tuple}")
print(f"Type is : {type(my_tuple)}")
my_tuple = (9,)
print(f"Contents: {my_tuple}")
print(f"Type is : {type(my_tuple)}")
# Access element
my_tuple = (1, 2, 3, 4, 5)
# 1st element
print(f"First element: {my_tuple[0]}")
# 2nd element
print(f"Second element: {my_tuple[1]}")
# Last element
print(f"Last element: {my_tuple[-1]}")
# 2nd to last element
print(f"Second to last element: {my_tuple[-2]}")
# Tuple assignment is interesting - assign a tuple of variables to a tuple of values & map them
# Sometimes called tuples packing and unpacking. Both tuples need the same number of elements or else there will be a value error
tuple1 = ("Cisco", "2600", "12.4")
# Assign variables to tuple1
(vendor, model, ios) = tuple1
print(f"Vendor: {vendor}\n")
print(f"Model: {model}\n")
print(f"IOS: {ios}")
# Assign variables in one tuple to values in another in one statement
(a, b, c) = (10, 20, 30)
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
# Find out what methods/functions are available
a = ()
b = []
print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
print(f"Methods/functions available to a: {dir(a)}")
print(f"Methods/functions available to b: {dir(b)}")
# Find out the number of elements inside a tuple
tuple2 = (1, 2, 3, 4)
print(f"Length of tuple2: {len(tuple2)}")
# Lowest and greatest value in a tuple
print(f"Lowest value in tuple2: {min(tuple2)}")
print(f"Highest value in tuple2: {max(tuple2)}")
# Concatinate and multiply tuple
print(f"Concatinate tuples: {tuple2 + (5, 6, 7)}")
print(f"Multiply tuples: {tuple2 * 2}")
# Slicing is also possible with tuples
print(f"1st 2 elements inside the tuple: {tuple2[0:2]}")
print(f"[:2] returns the same: {tuple2[:2]}")
print(f"Slice from element 1 to the end of the tuple: {tuple2[1:]}")
print(f"Entire tuple: {tuple2[:]}")
print(f"Without the last 2 elements in the tuple: {tuple2[:-2]}")
print(f"Without the first 2 elements in the tuple: {tuple2[-2:]}")
print(f"Insert a step in the slice to show in reverse order: {tuple2[::-1]}")
# Check if an element is a member of a tuple or not
print(f"Is 3 in tuple2: {3 in tuple2}")
print(f"Is 3 not in tuple2: {3 not in tuple2}")
print(f"Is 5 in tuple2: {5 in tuple2}")
# To delete the entire tuple
del tuple2 # This will throw an error if you try to print the tuple as it not defined anymore

