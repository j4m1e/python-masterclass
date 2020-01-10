"""
Functions. To create reusable code blocks. 
"""
def myFirstFunction():
    # doc string below which can be used a help section using help(myFirstFunction)
    "This is a function"
    print(f"Hello Python!")
# get help on the function that has been created
help(myFirstFunction)
# call the function
myFirstFunction()
# parameters
def mySecondFunction(x):
    "This prints out the parameter that is passed to it as an argument"
    print(f"{x}")
# call the function
mySecondFunction("Hello Python")
# more than one parameter
def myThirdFunction(x, y):
    print(f"Hello {x}")
    print(f"Hello {y}")
# call the function
myThirdFunction("Python", "Javascript")
# return - used to exit a function and return something whenever the function is called
# without a variable for return it would be like saying return none
def mySum(x, y):
    sum = x + y
    return sum
# call the function
print(f"{mySum(1, 2)}")
# more complex return
def mySum2(x, y, z):
    sum = (x + y) * z
    return sum ** 2
# call the function - should return 81. (1+2)*3=9^2=81
print(f"{mySum2(1, 2, 3)}")
# return none
def mySum3(x, y, z):
    sum = (x + y) * z 
    return 
# call the function
mySum3(1, 2, 3) 