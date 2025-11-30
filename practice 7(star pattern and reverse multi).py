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

#for rectangle = basically check if first column and last column is i or not if yes print "*" there
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()

#to print reverse table
n = 5
for i in range(10,0,-1):   #(starts on 10,stops at 0, and goes back by -1)
    print(n*i)