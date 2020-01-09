"""
New to Python 3.6, this provides an elegant way to insert variables into a string. 
Formula can also be inserted into the string in relation to the variable
"""
carManufacturer = "Mercedes"
model = "GLC 300 AMG Line"
variant = "Premium Plus"
colour = "Red"
quantity = 1

print(f"Manufacturer: {carManufacturer}\n")
print(f"Model: {model} Variant: {variant}\n")
print(f"Colour: {colour} Quantity: {quantity * 4}")

# add a method to a variable
print(f"Manufacturer: {carManufacturer}\n")
print(f"Model: {model} Variant: {variant}\n")
print(f"Colour: {colour.upper()} Quantity: {quantity * 4}")