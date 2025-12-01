#greatest of three numebers
def greatest(num1,num2,num3):
    if num1 > num2 and num1>num3:
        print(num1,"is greatest")
    elif num2>num1 and num2>num3:
        print(num2,"is greatest")
    else:
        print(num3,"is greatest")

greatest(2,4,3)

#celsius to fahrenheit
def makefahrenheit(celsius):
    fahrenheit = ((9/5)*celsius)+32
    print(fahrenheit,"F")

makefahrenheit(36)

#sum of first n natural number using recursion
def natural(n):
    if n == 1:
        return 1
    else:
        return n+natural(n-1)

print(natural(5))

#reverse right angle triangle
def lines(n = 3):
    if n == 0:
        return 
    print("*"*n)
    lines(n-1)

lines(3)


#inches to cms
def makecms(inches):
    cms = inches*(2.54)
    print(cms,"cms")
makecms(74)

#remove a given word
def clean_list(words, target):
    # strip each string and keep only those not equal to target
    return [w.strip() for w in words if w.strip() != target]

lst = ["  hello ", " world", " test ", "hello  "]
print(clean_list(lst, "hello"))   # ['world', 'test']

#table using function
def table(n):
    for i in range(1,11):
        print(n*i)

table(5)