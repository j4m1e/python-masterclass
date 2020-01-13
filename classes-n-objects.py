"""
Classes & Objects. This is object orientated programming (OOP), this is based on classes, objects and methods. A class
is its own data type containing its own variables, attributes and functions (in OOP these are called methods). A standard
definition of a class is that it is a blueprint for creating objects. An object is an instance of a defined class and the
attribute values for a particular object define the state of that object. Another term that is used with classes is
inheritance, this means that the new class may inherit all the names and functionality from an existing class  
"""
# define a class. The convention is to use camel case in the class name. If the class doesnt inherit from another class
# then the word object (inherits from the default object class) should be used within the perentheses 
class MyRouter(object):
    # doc string like functions can be used here
    "This is a class that describes the characteristics of a router."
    # first thing to define within the class is the special init method also called a class constructor
    # the role of init is to initialise some variables and the method is called whenever a new instance of the class is 
    # created in which it resides. Every class method has to have the parameter self (reference to the current instance 
    # of the class)
    def __init__(self, routername, model, serialno, ios):
        # instance/object attributes to describe the router according to parameters of the init method
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    
    def printRouter(self, manufDate):
        # print out the attributes and concatinate the model of the router and the manufacturing date
        print(f"The router name is {self.routername}")
        print(f"The router model is {self.model}")
        print(f"The router serial number is {self.serialno}")
        print(f"The IOS version is {self.ios}")
        print(f"The model and date combined is {self.model}{manufDate}")

# an object is an instance of the class, as many objects as required can be created by calling the class name
# and entering the required arguments required by the init method in between parenthensis except self which is
# passed by Python automatically
print(f"Creating an object from the class MyRouter called router1")
router1 = MyRouter("R1", "2600", "123456", "12.4")
print(f"{router1}")
# access each of the objects attributes
print(f"Accessing the router1 objects attritubes")
print(f"The name of the router is {router1.routername}")
print(f"The model is {router1.model}")
print(f"The serial number is {router1.serialno}")
print(f"The IOS version is {router1.ios}")
# access the method defined inside the class. Self is invoked by Python so doesnt need to be included
print(f"Accessing the class method printRouter for object router1")
router1.printRouter("20181010")
# create another object router2
print(f"Creating another object from the class MyRouter called router2")
router2 = MyRouter("R2", "7200", "101010", "12.2")
print(f"{router2}")
# access each of the objects attributes
print(f"Accessing the router2 objects attritubes")
print(f"The name of the router is {router2.routername}")
print(f"The model is {router2.model}")
print(f"The serial number is {router2.serialno}")
print(f"The IOS version is {router2.ios}")
# access the method defined inside the class. Self is invoked by Python so doesnt need to be included
print(f"Accessing the class method printRouter for object router2")
router2.printRouter("20190101")
# change an attribute of an object
print(f"Changing the IOS attribute of router2")
print(f"It is currently {router2.ios}")
router2.ios = "12.3"
print(f"It is now {router2.ios}")
# Python provides some functions to affect object attributes
# getattr function is to get the value of an attribute
print(f"Get the value of attribute ios of the router2 object {getattr(router2, 'ios')}")
# setattr function is to set a new value for an attribute
setattr(router2, "ios", "12.1")
print(f"Set the ios attribute value to 12.1 for the router2 object. It has been set to {getattr(router2, 'ios')}")
# hasattr function checks to see if an attribute exists or not
print(f"Does the router2 object have the attribute of ios: {hasattr(router2, 'ios')}")
print(f"Does the router2 object have the attribute of ios2: {hasattr(router2, 'ios2')}")
# delattr function deletes an attribute
print(f"Deleting the attribute ios of router2")
delattr(router2, "ios")
print(f"Does the ios attribute for router2 exist: {hasattr(router2, 'ios')}")
"""
if getattr is used to retreive an object that doesnt exist
getattr(router2, "ios")
This would yield 
AttributeError: 'MyRouter' object has no attribute 'ios'
"""
# verify that an object is an instance of a particular class
print(f"Check that router2 is an instance of the MyRouter class: {isinstance(router2, MyRouter)}")
"""
Class Inheritance. Have one class that inherits attributes and methods from an existing class. The class inheriting
the attributes and methods is a child class and the class that the child inherits from is called a parent. To inherit
from a certain class the name of the class is placed between the parenthensis of the child class definition instead of
object. 

A child class can inherit from 2 or more parents at the same time. This is achieved by the following.
'class ChildClass(ParentClass1, ParentClass2, ParentClass3):'
"""
# define the new class. The init method for a child class can be omitted as the child extends the parent class and
# therefore inherited from the parent. If there are new attributes to define as well as inheriting then the init
# method needs to be redefined but telling Python to inherit the attributes and also add the new ones
print(f"CLASS INHERITANCE")
class MyNewRouter(MyRouter):
    # inserted all the attributes from the parent class plus the new attribute for the child (portsno)
    def __init__(self, routername, model, serialno, ios, portsno):
        # call the init method from the parent class. which is like importing them from the parent class
        MyRouter.__init__(self, routername, model, serialno, ios)
        # define the new attribute specific to this class only called portsno 
        self.portsno = portsno 
    # define a method inside the child class that concatinates a string argument when calling the method & the value
    # of the model attribute inherited from the parent
    def printNewRouter(self, string):
        print(f"{string}{self.model}")

print(f"Creating an object from the class MyNewRouter called newRouter1")
newRouter1 = MyNewRouter("newr1", "1800", "11111", "12.2", "10")
print(f"{newRouter1}")
print(f"The portsno attribute for the object newRouter1 is {newRouter1.portsno}")
# access the attributes from the parent class using the instance of the child
print(f"The parent class attribute model is {newRouter1.model}")
print(f"The parent class attribute ios is {newRouter1.ios}")
# access a method from the parent class
print(f"Calling the parent class method printRouter()")
newRouter1.printRouter("20200101")
print(f"Calling the child class method printNewRouter()")
newRouter1.printNewRouter("20200101")
# check if a class is a child of another 
print(f"Is the class MyNewRouter a child of MyRouter: {issubclass(MyNewRouter, MyRouter)}")