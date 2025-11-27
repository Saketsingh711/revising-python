# practice 2

a = 30
b = 80

if(a>b):
    print("A is greater than B")
else:
    print("B is grater than A")

c = int(input("Enter first number: "))
d = int(input("Enter second number: "))

avg = (c+d)/2
square = (c*c)

print(avg)
print(square)

#indicing where [0:3] 0th element is included but 3rd element is excluded while in negative indexing the last element is index -1 and in positive first element is index 0
name = "Saket"
sl = name[0:3]
print(sl)

print(name[0:5:2]) #skips every second element
