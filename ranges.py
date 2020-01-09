"""
Ranges.
Python2 would be as follows
print range(10) would yeild [0,1,2,3,4,5,6,7,8,9]
print range(5,10) would yeild [5,6,7,8,9]
print range(0,10,2) woud yeild [0,2,4,6,8] 
print range(-2,-10,-2) would yield [-2,-4,-6,-8]
xrange() is an iterator and only produces the value when asked
"""
r = range(10)
print(f"r: {r}")
print(f"Type of r: {type(r)}")
# List instead of range
print(f"List: {list(r)}")
# To elements from range use indexes
print(f"1st element in range: {r[0]}")
print(f"Last element in range: {r[-1]}") 
# Find if an element is a member of the range
print(f"Is 10 in the range: {10 in r}")
print(f"Is 7 not in the range: {7 not in r}")
print(f"Is 7 in the range: {7 in r}")
# Use the index method to find out the index of an element in the range
print(f"Index of 4: {r.index(4)}")
# Cannot apply a slide to a range but can convert to a list to do it
print(f"Return 2,3,4: {list(r)[2:5]}")