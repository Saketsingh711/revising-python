#storing information of programmers working at microsoft
class Programmer:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
    
    def get_info(self):
        print(f"{self.name} = {self.occupation}")

programmer1 = Programmer("Rakesh","Developer")

programmer1.get_info()


#creating calculator

class Calculator:
    def __init__(self,number):
        self.number = number
    
    def square(self):
        return self.number*self.number
    
    def cube(self):
            return self.number*self.number*self.number

    def squareroot(self):
            return self.number ** 0.5   #raising power to 0.5

obj1 = Calculator(16)

print(obj1.squareroot())