#super() = Function used in a child class to call methods from a parent class and also allows to extend the functionality of the inherited methods


# super().__init__() #this will call constructor of the base class along with the methods that will be given


#class method
class Student:
    count = 0 
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
    
    def get_info(self):       #instance method will work on object
        return f"{self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):      #classmethod will work on class
        return f"Student count is {cls.count}"
    
student1 = Student("Saket",9.5)
print(student1.get_info())    #instance method called
print(Student.get_count())    #classmethod called