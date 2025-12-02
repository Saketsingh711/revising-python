import random as r
#to check if poems.txt has the word Twinkle
with open("poems.txt","r") as p:
    text = p.read()
    if "Twinkle" in text:
        print("yes")
    else:
        print("no")


# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.        
score = 0
def game(player):
    global score
    comp = r.randint(0,3)
    print("You guessed : ",player)
    print("The number was : ",comp)
    if (player == comp):
        print("You guesssed right")
        score = score + 1
    else:
        print("You guessed wrong")

file = open("Hi-score","w")

n = int(input("Enter your guess (0-3): "))
game(n)
print("Your score is:", score)
print("----------------------")

s = str(score)
print(s)
file.write(s)        #update score in Hi-score.txt
file.close()



#to make tables till 20 and make different files
# def table(number):
#     with open(f"Table{number}.txt","w") as f:
#         for i in range(1,11):
#             line = f"{number} * {i} = {number * i}\n"
#             print(line,end =" ")
#             f.write(line)
      
# for num in range(2,21):
#     print(f"\n----- Table of {num} -----")
#     table(num)
