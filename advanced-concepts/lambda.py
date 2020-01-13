"""
Lambda functions. Python allows for the creation of small anonymous functions are runtime and these are called
lambda functions. Easy way to insert functionality into code especially in places which would not allow for 
the creation of regular functions. Unlike regular functions, a lambda function can be embedded wherever required
inside the code and they do not need a return statement to output something from that function. Although not 
mandatory a lambda function can be assigned to a variable so that variable can be used elsewhere in the program. 
If it isnt then the lambda function will immediately run where its put in the code.  

Lambda is used alot with map() and filter() functions

General syntax for a lambda function

lambda arg1, arg2, ... , argn: an expression using the arguments
"""
print(f"LAMBDA FUNCTIONS")
print(f"Simple lambda function to multiply to arguments together")
a = lambda x, y: x * y 
print(f"{a}")
print(f"{type(a)}")
print(f"Executing the lambda function usings values 2 and 10: {a(2, 10)}")
"""
lambda function with list comprehension which has a nested for loop. Tradional way of doing it. Update a list containing
all the elements by multiplying each element in the range 0 through 9 with each element in the range 0 through 4 and concatinate
this list with a list that is passed as an argument to the function. 

def myFunc(myList):
    listXy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            listXy.append(result)
    return listXy + myList

myFunc([100, 101, 102])
"""
print(f"Complex lambda function that multiplies one range by another and then concatinates another list to it")
b = lambda myList: [x * y for x in range(10) for y in range(5)] + myList
print(f"{b}")
print(f"{type(b)}")
print(f"Executing lambda function which muliples 0-9 by 0-5 and concatinates a list that is passed as an argument")
print(f"{b([100, 101, 102])}")
