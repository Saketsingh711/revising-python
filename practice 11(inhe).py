# Create a class (2-D vector) and use it to create another class representing a 3-D vector
class vector1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def funct(self):
        return f"Hello {self.x} = {self.y} = {self.z}"
    
class vector2(vector1):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z

vector = vector2(5,6,7)

print(vector.funct())


# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self,d):
        self.d = d

class Pets(Animals):
    def __init__(self, d):
        super().__init__(d)
    

class Dog(Pets):
    def __init__(self, d):
        super().__init__(d)

    def bark(self):
        return f"{self.d} barks"
    
dog1 = Dog("tommy")
print(dog1.bark())


#Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary          # base salary
        self.increment = increment    # e.g. 0.10 for 10%

    @property
    def salaryAfterIncrement(self):
        return int(self.salary * (1 + self.increment))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,new_salary):
        self.increment = (new_salary/self.salary) -1

    
e = Employee(10000,0.1)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 12000
print(e.increment)


# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them
class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self,other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
    
    def __mul__(self,other):
        return f"{self.real * other.real} * {self.imaginary * other.imaginary}i"
c1 = Complex(5,6)
c2 = Complex(7,8)

print(c1+c2)
print(c1*c2)


#Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, components):
        self.data = components  # list/tuple of numbers

    def __str__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.data, other.data)])

    def __mul__(self, other):
        return sum(x * y for x, y in zip(self.data, other.data))

    def __len__(self):
        return len(self.data)

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 =", v1)           
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v1 * v2 =", v1 * v2)
print(f"The Vector has {len(v1)} dimensions.")


#
class Vector1:
    def __init__(self,components):
        self.data = components
    
    def __str__(self):
        a,b,c = self.data
        return f"{a}i + {b}j + {c}k"
    
v3 = Vector1([7,8,10])
print(v3)

