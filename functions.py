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
print(f"PARAMETERS")
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
# arguments. The basic argument is positional i.e. the number of arguments should be the same as parameters
# if they are different then a type error will be thrown
def myFourthFunction(x, y, z):
    sumXyz = (x + y) * z
    return sumXyz
"""
if the above was called
myFourthFunction(1, 2)
This would throw the error - TypeError: myFourthFunction() missing 1 required positional argument: 'z'
"""
# keyword argument. allow for the order to be ignored or some to be skipped. 
print(f"KEYWORD ARGUMENTS")
print(f"{myFourthFunction(x = 1, y = 2, z = 3)}")
# change the order 
print(f"{myFourthFunction(z = 3, x = 1, y = 2)}")
# positional and keyword arguments can be mixed but positional must be first (rule) otherwise Python will 
# throw a syntax error
print(f"POSITIONAL & KEYWORD ARGUMENTS")
print(f"{myFourthFunction(1, 2, z = 3)}")
# default value for an argument. Can be overwritten by passing the argumnet or can be omitted for the default 
print(f"DEFAULT PARAMETERS")
def myFifthFunction(x, y, z = 3):
    sumXyz = (x + y) * z 
    return sumXyz
# call the function
print(f"{myFifthFunction(1, 2)}")
print(f"{myFifthFunction(1, 2, 4)}")
# Don't know the number of parameters needed so want variable number of parameters in the function
# user args which is a tuple of additional parameters. If no additional parameters are supplied then the tuple
# is empty. Doesnt have to be args and kwargs its the * and ** that informs python if its positional or keyword
print(f"VARIABLE PARAMETERS IN A FUNCTION")
# positional parameters
def mySixthFunction(x, *args):
    print(f"{x}")
    print(f"{args}")
    print(f"Print the positional arguments in a nice way")
    for argument in args:
        print(f"{argument}")
# call the function
mySixthFunction("Hello")
mySixthFunction("Hello", 100, 200)
# keyword parameters will be a list not a tuple
def mySeventhFunction(x, **kwargs):
    print(f"{x}")
    print(f"{kwargs}")
    print(f"Print keyword arguments in a nice way")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# call the function
mySeventhFunction("Hello")
mySeventhFunction("Hello", y = 100, z = 200)
