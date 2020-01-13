"""
List, set & dictionary comprehensions. Build sequences from other sequences in an easy, quick and elegant way. 

List comprehensions are widely used and a quick alternative to something that has already been used (for loop). 
Iterate over a list and perform any action on each of its elements

list1 = []
for i in range(10):
    result = i ** 2
    list1.append(result)
print(f"{list1}")

To do this in a single line with a list comprehension

Before the 'for' this is the action to be performed on each element followed by the loop structure
"""
print(f"LIST COMPREHENSIONS")
print(f"From 0 to 9, perform a square of the value")
list1 = [x ** 2 for x in range(10)]
print(f"{list1}")
# add a conditional statement within the loop construct 'list = [action loop condition]'
print(f"Add a condition that only 6 - 9 (>5) will be squared")
list2 = [x ** 2 for x in range(10) if x > 5]
print(f"{list2}")
# set comprehensions
print(f"SET COMPREHENSIONS")
print(f"From 0 to 9, perform a square of the value")
set1 = {x ** 2 for x in range(10)}
print(f"set1 has the type of {type(set1)}")
print(f"{set1}")
# dictionary comprehensions
print(f"DICTIONARY COMPREHENSIONS")
print(f"From 0 to 9, perform a square of the value")
dict1 = {x : x ** 2 for x in range(10)}
print(f"dict1 has the type of {type(dict1)}")
print(f"{dict1}")