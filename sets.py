"""
Sets. Unordered collection of unique elements. Think lists that no duplicate elements. 
These are mutable so elements can be added and removed. 
"""
# Create a set (2 ways)
# 1st way
list4 = [1, 2, 3, 4, 5, 2, 3]
print(f"Contents of list4: {list4}")
print(f"Set created from list 4: {set(list4)}") # this will remove duplicate elements
set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(f"Set created using a variable: {set1}")
# Check type of set1
print(f"Type of set1 is {type(set1)}")
# 2nd way
set2 = {11, 12, 13, 14, 15, 15, 15, 11}
print(f"Set2 created using curly braces: {set2}")
print(f"Type of set2 is {type(set2)}")
# Find out the number of elements in a set
print(f"Number of elements in set2: {len(set2)}")
# Check if an element is part of a set
print(f"Is 11 part of set2: {11 in set2}")
print(f"Is 10 part of set2: {10 in set2}")
print(f"Is 10 not part of set2: {10 not in set2}")
# Add to set - will not throw an error if it already in the set. Just doesn't add it
print(f"Set2: {set2}")
set2.add(16)
print(f"Added 16 to set2: {set2}")
# Remove from a set
set2.remove(11)
print(f"Removed 11 from set2: {set2}")
# Methods
set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}
# Common elements in both sets
# Intersection
print(f"Find set1 intersection with set2: {set1.intersection(set2)}")
print(f"Find set2 intersection with set1: {set2.intersection(set1)}")
# Differences between both sets
# Difference
print(f"Find the difference between set1 and set2: {set1.difference(set2)}")
print(f"Find the difference between set2 and set1: {set2.difference(set1)}")
# Unify the two sets
# Union (this does not concatinate - unique elements)
print(f"Create an union between set1 and set2: {set1.union(set2)}")
# Remove a random element in the set
# Pop
print(f"Original set1: {set1}")
set1.pop()
print(f"Random element removal in set1: {set1}")
# Clear a set
# Clear
print(f"Original set1: {set1}")
set1.clear()
print(f"Cleared set1: {set1}")
# Frozensets are immutable sets i.e. cannot be changed
# Could be used as an element in another set or a key in a dictionary
# add and remove attributes are not available for frozensets
list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]
fs1 = frozenset(list1)
fs2 = frozenset(list2)
print(f"fs1: {fs1}")
print(f"fs2: {fs2}")
print(f"Type of fs1: {type(fs1)}")
# Common elements in both sets
# Intersection
print(f"Find fs1 intersection with fs2: {fs1.intersection(fs2)}")
print(f"Find fs2 intersection with fs1: {fs2.intersection(fs1)}")
# Differences between both sets
# Difference
print(f"Find the difference between fs1 and fs2: {fs1.difference(fs2)}")
print(f"Find the difference between fs2 and fs1: {fs2.difference(fs1)}")
# Unify the two sets
# Union (this does not concatinate - unique elements)
print(f"Create an union between fs1 and fs2: {fs1.union(fs2)}")
 
