class Employee:
    company = "gogle"#class attribute
    def getsalary(self):  #self referes to instance of the class
        print("Salary is not there") 

    @staticmethod #explained below 
    def greet():
        print("Hello")

harry = Employee()
print(harry.company)
harry.name = "harry"      #instance(object) attribute
print(harry.name)


harry.getsalary()      #here self becomes harry

# @staticmethod is a method that belongs to class not object. therefore when you call a staticmethod you need class name rather than object name and you also wont need self keyword
Employee.greet()

#__init__ is the constructor which is first run as the object is created (initializes the object)