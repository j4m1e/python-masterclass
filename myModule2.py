myVar = 10
def myFunction():
    print(f"This is the function inside in the module!")

# stop code executing on import of module
# if this code is executed as a standalone file then execute the code below in addition to the rest of the code
# if this code is imported as a module then do not execute the code below the 'if'
if __name__ == "__main__":
    print(f"This will be executed")