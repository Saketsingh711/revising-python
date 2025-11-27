# 
num = 5
for i in range(1,11):
    print(f"5 * {i} = {num*i}")

#
l = ["Harry","Soham","Sachin","Rahul"]
for i in l:
    if i.startswith("S"):    #function to check the start word
        print("Hello "+i)