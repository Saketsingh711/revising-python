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
    
    @staticmethod
    def greet():
         print("Hello user")
obj1 = Calculator(16)
Calculator.greet()
print(obj1.squareroot())


###
class test:
     a = 2

test1 = test()
test1.a = 0

print(test.a)
print(test1.a)#so it does not change the class attribute


#booking ticket, checking status,and get fare information of train
class train:
    def __init__(self,trainname,total_seats = 100):
        self.trainname = trainname
        self.total_seats = total_seats
        self.booked_seats = 0 
    
    def get_fare(self):
        if self.trainname == "Shatabdi Express":
            return 2000
        elif self.trainname == "Gyan Ganga":
            return 3000
        else:
            return 1000
    
    def book_ticket(self,n=1):
        if n<=0:
            print("Invalid number of tickets")
            return
        if self.booked_seats + n <= self.total_seats:
            self.booked_seats += n
            print(f"{n} ticket(s) booked for {self.trainname}")
            print(f"Total fare: Rs.{self.get_fare() *n}")
        else:
             print("Not enough seats")
    
    def get_status(self):
        available = self.total_seats - self.booked_seats
        print(f"Train : {self.trainname}")
        print(f"Total seats : {self.total_seats}")
        print(f"Booked Seats : {self.booked_seats}")
        print(f"Available seats : {available}")


train1 = train("Shatabdi Express")
train1.get_fare()
train1.book_ticket(10)
train1.get_status()