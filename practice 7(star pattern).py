#print right angle triangle
n = 6
for i in range(1,n+1):
    for j in range(i):
        print("*",end = "")
    print()
#or
for i in range(1,n+1):
    print("*"*i)


#print pyramid
for i in range(1,n+1):
    space = " "*(n-i)
    stars = "*"*(2*i-1)
    print(space+stars)
#or (any method can be used)
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end = " ")
    for k in range(2*i-1):
        print("*",end = " ")
    print()