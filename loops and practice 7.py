# # 
# num = 5
# for i in range(1,11):
#     print(f"5 * {i} = {num*i}")

# #
# l = ["Harry","Soham","Sachin","Rahul"]
# for i in l:
#     if i.startswith("S"):    #function to check the start word
#         print("Hello "+i)

# # 
# num = 5
# i = 1
# while(i<11):
#     print(f"5 * {i} = {num*i}")
#     i = i + 1

# # to check prime number
# num = int(input("Enter a number to check if it is prime or not: "))
# count = 0
# if num <= 1:
#     print("not prime")
# else:
#     for i in range(2,num-1):
#         if num % i == 0:
#             count = 1

#     if count == 1:
#         print("not prime")
#     else:
#         print("prime")

# # sum of n natural numbers
# limit = int(input("Enter the limit for sum of natural numbers: "))
# total = 0
# for i in range(1,limit+1):
#     total = total+ i

# print(total)

# factorial
num1 = int(input("Enter the number for factorial: "))
fact = 1
for i in range(1,num1+1):
    fact = fact*i

print(fact)