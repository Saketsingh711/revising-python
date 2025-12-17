import random as r
cchoice = r.randint(1,10)
count = 0
while True:
    pchoice = int(input("Enter a number between 1-10 = "))

    if cchoice == pchoice:
        print("Correct Number")
        print(f"You took {count} tries to guess.")
        break
    elif cchoice > pchoice:
        print("Higher Number please")
        count = count+1
    else:
        print("Lower Number please")
        count = count+1
    
