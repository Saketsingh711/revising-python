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


#GETTER SETTER DECORATOR
class Student:
    def __init__(self, name, grade):
        # private attribute (convention: underscore prefix)
        self._name = name
        self._grade = grade

    @property
    def grade(self):
        """
        Getter method for grade.
        Allows controlled access to the private _grade attribute.
        """
        return self._grade

    @grade.setter
    def grade(self, value):
        """
        Setter method for grade.
        Adds validation before updating the private _grade attribute.
        """
        if 0 <= value <= 100:
            self._grade = value
        else:
            raise ValueError("Grade must be between 0 and 100.")

# Example usage
student1 = Student("Saket", 85)

print("Initial Grade:", student1.grade)   # calls getter

student1.grade = 92                       # calls setter
print("Updated Grade:", student1.grade)

# student1.grade = 150  # ❌ raises ValueError