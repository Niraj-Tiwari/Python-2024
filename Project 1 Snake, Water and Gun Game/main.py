'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youStr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reversedDict = {1:"s",-1:"w",0:"g"}
you = youDict[youStr]

# By now, we have two numbers(variables), you and computer

print(f"Computer chose\n {reversedDict[computer]} You chose {reversedDict[you]}")

if(computer == you):
    print("There is a draw(tie)")

else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went wrong")


