"""
Itertools library. This library includes a lot of functions for working with iterable datasets
"""
from itertools import *
list1 = [1, 2, 3, "a", "b", "c"]
list2 = [101, 102, 103, "X", "Y"]
"""
chain()
Takes several sequences as arguments and chains them together. 
"""
print(f"CHAIN()")
print(f"iterate with a for loop")
for i in chain(list1, list2):
    print(f"{i}")
print(f"use the list function: {list(chain(list1, list2))}")
"""
count()
Returns an iterator that generates consecutive integers until it is stopped otherwise it will
be infinite.
"""
print(f"COUNT()")
print(f"iterate with a for loop, starting at 10 and incrementing by 2.5")
# count function starting point is 10 and 2.5 is the step to increment by
for i in count(10, 2.5):
    # less than or equal to 50
    if i <= 50:
        print(f"{i}")
    else:
        # break out of the loop
        break 
"""
cycle()
Returns an iterator that repeats the value given as an argument infinately

a = range(11, 16)
for i in cycle(a):
    print(f"{i}")

This will print infinately 

filterfalse()
Will return the elements that the function that is passed to it returns false
"""
print(f"FILTERFALSE()")
print(f"Returns the values in the list that did not match the < 5 for the range 1 to 7")
print(f"{list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7]))}")
"""
islice()
Same as list and string slices. A start and end point can be specified and a step 

range(10)
list(range(10))
list(range(10))[2:9:2]

The result would be [2, 4, 6, 8]
"""
print(f"ISLICE()")
print(f"from a range of 0 to 9, start at 2 and up to (but not including) 9 with a step of 2")
print(f"{list(islice(range(10), 2, 9, 2))}")

