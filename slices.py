"""
Take a string variable and only return part of the variable string
string1[start:stop:step]
"""
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

# Extract the first IP Address
# start slice value is to the left of the colon and up to but not including is the end value
print(string1[5: 15])

# If the end slice index is missing then its from the start index to the end of the string
print(string1[5:])

# If the start slide index is missing then its from the beginning of the string to the end index
print(string1[:15])

# Return the whole string
print(string1[:])

# Negative indexes 
# Last character of string would be achieved by using -1
print(string1[-1])
# -2 would return the second to last
print(string1[-2])
# And with slices to return the string Ethernet
print(string1[-9:-1])
# Last 5 characters
print(string1[-5:])
# Everything except the last 5 characters
print(string1[:-5])
# Use step i.e. skip every second character of the string
print(string1[::2])
# String in reverse order
print(string1[::-1])

mystring = "0123456789"
# Even
print(mystring[::2])
# Odd
print(mystring[1::2])
# Odd but less than 7
print(mystring[1:7:2])


