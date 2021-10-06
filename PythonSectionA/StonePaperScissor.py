# Stone Paper Scissor
import random
userScore = 0
cpuScore = 0
options = ['stone','paper','scissor']
game = True
while game:
    cpu = random.choice(options)
    user = input("Enter your choice : ")
    print("CPU :",cpu)
    if cpu == user:
        print("Match Tie")
    elif cpu == "stone" and user == "scissor":
        print("CPU Win")
    elif cpu == "paper" and user == "stone":
        print("CPU Win")
    elif cpu == "scissor" and user == "paper":
        print("CPU Win")
    elif cpu == "stone" and user == "paper":
        print("You Win")
    elif cpu == "paper" and user == "scissor":
        print("You Win")
    elif cpu == "scissor" and user == "stone":
        print("You Win")
