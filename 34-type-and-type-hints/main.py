# set the data type for a variable

# age: int
# name: str
# is_friendly: bool

# can do this in a function where the paramaters go to tell the function the data type it should expect
# here we are telling the function that we are expecting an input age of type int

def check(age: int):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    
    return can_drive

# we can also declare in the function what the expected output
# here we are telling the function that we are expecting an input age of type int and an output of type bool
# IMPORTANT NOTE - using the arrow to define the expected output will not result in a type error like when declaring
# the parameter type above, it relies on the interpreter presenting that information to the user

def check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
        
    return can_drive