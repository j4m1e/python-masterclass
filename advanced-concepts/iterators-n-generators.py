"""
Iterators & Generators. 

An iterator is an object which allows a programmer to go through all the 
elements of a collection sequence regardless of its specific implementation. This is the iter()
function that takes an iterable object as an argument and returns an iterator 
"""
print("INTERATORS")
myList = [1, 2, 3, 4, 5, 6, 7]
print(f"myList is {myList}")
"""
To print all the elements out a for loop could be used 
for element in myList:
    print(f"{element}")
"""
myIter = iter(myList)
print(f"The type of myIter is {type(myIter)}")
# to iterate through myIter the next() function can be used
print(f"{next(myIter)} {next(myIter)} {next(myIter)} {next(myIter)} {next(myIter)}")
print(f"{next(myIter)} {next(myIter)}")
# once the end of the sequence is reached the StopIteration is thrown
"""
A generator is a special routine can be used to control the iteration behaviour of a loop. This is
similar to a function it is defined using the 'def' keyword, can have parameters and can be called. 
As apposed to a function which returns an entire array with all the values a generator function 
yields the values one at a time. This is sometimes called a resumable function. The sequence can be
traversed up to certain point, get the result and suspend the execution. Later, that point can be 
returned to and resume the execution. This is a great advantage as this way less memory is required   
"""
print(f"GENERATORS")
def myGen(x, y):
    # iterate over the range of x
    for i in range(x):
        # print the values of i and y 
        print(f"i is {i}")
        print(f"y is {y}")
        # yield the result of multiplying each element in range of x with y
        # the 'yield' keyword suspends the function execution and sends the value back to the caller
        # it also saves the state of the execution so when the execution is resumed it picks up after
        # the yield statement
        yield i * y 
myObject = myGen(10, 5)
print(f"{myObject}")
print(f"The type of myObject is {type(myObject)}")
print(f"Run for the first time")
print(f"{next(myObject)}")
print(f"Run for the second time")
print(f"{next(myObject)}")
# at the end of the object is reached the StopIteration is thrown
"""
Generator expressions. Similar to comprehensions only they use () not []
"""
print(f"Generator Expressions")
genExp = (x for x in range(5))
print(f"{genExp}")
print(f"The type of genExp is {type(genExp)}")
# iterate through genExp using the next() function
print(f"{next(genExp)} {next(genExp)} {next(genExp)} {next(genExp)} {next(genExp)}")
# at the end of the generator expression is reached the StopIteration is thrown