import random as r
while True:
    choice = int(input("Enter either Snake[1], water[2] or Gun[3]: "))
    pc = r.randint(0,2)
    def check(choice,pc):
        if (choice == pc):
            return 0
        elif (choice == 1 and pc == 2):
            return 1
        elif (choice == 1 and pc == 3):
            return -1
        elif (choice == 2 and pc == 1):
            return -1
        elif (choice == 2 and pc == 3):
            return 1
        elif (choice == 3 and pc == 1):
            return 1
        else:
            return -1
    score = check(choice,pc)
    print("You chose : ",choice)
    print("PC chose : ",pc)
    if(score == 0):
        print("Draw.")
    elif(score == 1):
        print("You won")
        break
    elif(score == -1):
        print("PC won")
        break
    else:
        print("Invalid Input")