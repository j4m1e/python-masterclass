"""
Decorators. This is a function that takes another function as a parameter and extends its functionality and behaviour without 
modifying it. Think of a decorator as a sweet wrapper, take a sweet a wrap it in a nice wrapper. The sweet is not altered in
any way.   
"""

def myDecorator(targetFunction):
    # inner function which concatinates targetFunction() being the sweet
    def functionWrapper():
        message = "Python is such a " + targetFunction() + " language!"
        return message
    # decorator returns the inner function as the result
    return functionWrapper

# to decorate a function 
@myDecorator
def targetFunction():
    message = "cool"
    return message

# call the function
print(f"{targetFunction()}")