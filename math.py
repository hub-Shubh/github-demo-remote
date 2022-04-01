#Add impletention
def add(x,y):
    return x+y

#Subtract implementation
def sub(x,y):
    return x-y              #on master branch

#Multiply implementation
def multiply(x,y):
    return x*y                  #on Bug456 branch

#Divide implementation

def divide(x,y):                #On master branch
    if y == 0:
        return DIVIDE_BY_0_ERROR
    else
        return x/y
