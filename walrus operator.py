#walrus operator(:=)
# #assigns values as variables as part of an expression.

if(n:=len([1,2,3,4,5]))>3:
    print(f"List is too long")

#without walrus we have to use n = len([1,2,3,4,5]) then we have to compare in if statement (n>3)


# TYPES DEFINITIONS IN PYTHON
# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types.
# Variable type hint
age: int = 25
# Function type hints        
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice")) # Output: Hello, Alice!
#here name:str defines that name should be string and -> str defines the return type to be string