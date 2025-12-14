#operator overloading using dunder(double underscore) methods
class ComplexNumber:
    def __init__(self,real_no,imaginary_no):
        self.real_no = real_no
        self.imaginary_no = imaginary_no

    def __add__(self,other):      #here self will be variable(a) and other will be variable(b)
        return f"{self.real_no+other.real_no} + {self.imaginary_no+other.imaginary_no}i"
    

a = ComplexNumber(5,7)
b = ComplexNumber(6,8)

print(a+b)          #before the function of line 7 this print would give error but after the function dunder method is used to remap its function


#same logic just used __gt__ as greater than
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __gt__(self,compare):
        if(self.age>compare.age):
            return True
        else:
            return False
    
p1  = Person("Chirag",21)
p2 = Person("Saket",19)

if (p1>p2):
    print(f"{p1.name} pays")
else:
    print(f"{p2.name} pays")