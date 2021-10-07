import random

options = ['stone','paper','scissor']
cpuScore = 0
userScore = 0
while True:
    cpu = random.choice(options)

    user = input("Enter your choice : ")
    print("CPU :",cpu)

    if user == cpu:
        print("Tie...")
    elif cpu == "stone" and user == "scissor":
        print("CPU Win")
        cpuScore += 1
    elif cpu == "paper" and user == "stone":
        print("CPU Win")
        cpuScore += 1
    elif cpu == "scissor" and user == "paper":
        print("CPU Win")
        cpuScore += 1
    elif cpu == "stone" and user == "paper":
        print("User Win")
        userScore += 1
    elif cpu == "paper" and user == "scissor":
        print("User Win")
        userScore += 1
    elif cpu == "scissor" and user == "stone":
        print("User Win")
        userScore += 1

    print("UserScore :",userScore)
    print("CpuScore :",cpuScore)

    if userScore == 5 or cpuScore == 5:
        break


