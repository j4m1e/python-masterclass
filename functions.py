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
# keyword parameters will be a dictionary not a tuple
def mySeventhFunction(x, **kwargs):
    print(f"{x}")
    print(f"{kwargs}")
    print(f"Print keyword arguments in a nice way")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# call the function
mySeventhFunction("Hello")
mySeventhFunction("Hello", y = 100, z = 200)
# Namespaces. This is a space holding some names. This is variables, functions or classes that are created
# This is a container holding the names that are defined where each name is associated with a namespace in 
# which it is defined. This way the same name can be defined in different namespaces. 
# There are 3 types of namespaces: built-in, global and local. The built-in namespace contains python's 
# built-in functions e.g. len(), max() and range(). The global namespace is where you define variables, 
# functions etc that have been imported into the program whereas the local namespace is used for names
# within a particular function  
print(f"NAMESPACES")
# built-in namespace
print(f"Built-in functions list() & range() which belong to the built-in namespace")
print(f"{list(range(10))}")
# global namespace
myVar = 10
print(f"Global variable which belongs to the global namespace")
print(f"{myVar}")
# local namespace
print(f"Local variable which belongs to the local namespace")
# If myVar2 = 10 is after the print statement then an error will be thrown. UnboundLocalError: local
# variable 'myVar2' referenced before assignment
def myVarFunction():
    myVar2 = 10 
    print(f"{myVar2}")
# call the function
myVarFunction()
# print(f"{myVar2 * 10}") would throw a NameError as myVar2 is not a global variable as it is local within the 
# function. Below using a global variable of the same name which will not throw a NameError
myVar2 = 20
print(f"{myVar2 * 10}")
# Use a global variable inside the local namespace of a function using global
print(f"Global variable used inside the local namespace of a function")
myVar3 = 5
def myVarFunction2():
    global myVar3
    print(f"{myVar3}")
# call the function
myVarFunction2()
# use the return statement with local variable so it can be accessed in the global namespace
print(f"Access a local variable in the global namespace using return")
def myVarFunction3():
    myVar4 = 10
    print(f"{myVar4}")
    return myVar4
# create a global variable and call the function
result = myVarFunction3()
print(f"{result * 10}")
# Modules. Just a python file that includes variables, functions and classes. Logically organise
# code. 
print(f"MODULES")
import math
print(f"functions available in the math module")
print(f"{dir(math)}\n")
# generally use the name of the module and then . to access the function
print(f"The value of PI is {math.pi}\n")
# user defined module
print(f"USER DEFINED MODULE")
# 1st way
# because there is a print statement within myModule this will get executed once on import
# this could be used to 'from myModule import *' but not recommended as it overloads the global namespace
# Python searches the current directory for the module and then the python path
# this can be shown by using the sys module as below
import sys
print(f"Python path: {sys.path}\n")
import myModule
# all the functions and variables are now available for use in this python code (global namespace)
# to prove that code is only executed once from the import
import myModule
# print out the varible from myModule
print(f"Variable (myVar) from myModule: {myModule.myVar}") 
# call the function from myModule
myModule.myFunction()
# 2nd way
# import some variables from the module into the global namespace as a different variable name
from myModule import myVar as myVar99
print(f"myVar99: {myVar99}") 
# importing another module which stops the executing of code on import
print(f"Import myModule2..")
import myModule2
print(f"Variable (myVar) from myModule2: {myModule2.myVar}")
# call the function from myModule2
myModule2.myFunction()
# How to find out how a module works or what functions, classes or variables are available to you
# use help to find out how to use the module
print(f"help() and dir() functions")
print(f"{help(sys)}")
# what names, functions, attributes are part of specified module namespace
print(f"{dir(sys)}")
# install a non standard module on windows
# 'python -m pip install openpyxl'
# to upgrade pip on windows
# 'python -m pip install --upgrade pip'