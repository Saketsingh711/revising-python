#list sotres value of any data type
friends = ["apple","akash","rohan",8,False]
#can be accessed by indexing
print(friends[0:5])

sample = [3,44,2,5,6,3]
sample.sort()
print(sample)
sample.reverse()
print(sample)
sample.append(2)
print(sample)
sample.insert(2,4)
print(sample)
sample.pop(2)
print(sample)
sample.remove(44)
print(sample)

#tuple = immutable data type
a = () #when nop element
b = (1,) #when 1 element comma is needed
c = (1,2,3,4) #more than 1 element

c.count(3)
c.index(1)

print(c.count(3))
print(c.index())
