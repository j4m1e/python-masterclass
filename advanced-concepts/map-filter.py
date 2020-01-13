"""
Map() & filter(). Very often used with lambda functions. 

The map() function takes a function and a sequence as arguments and applies the function to all 
the elements of the sequence returning an iterable object as the result. The function taken as 
the first argument can be a previously defined function or a lambda function. 
"""
print(f"MAP()")
print(f"Multiply each value in the range 0 to 9 by 10")
print(f"Normal function")
def product10(a):
    return a * 10

r1 = range(10)
print(f"{list(map(product10, r1))}")
print(f"Lambda function")
# use paranthesis around the lambda function for better readibility 
print(f"{list(map((lambda a: a * 10), r1))}")
"""
The filter() funcion also takes a function and a sequence as arguments and extracts all elements 
in the sequence for which the function returns true
"""
print(f"FILTER()")
print(f"Show only the elements in the range 0 to 9 that are greater than 5")
print(f"Lambda function")
print(f"{list(filter((lambda a: a > 5), r1))}")