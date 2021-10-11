import random
options = ['stone', 'paper', 'scissor']
cpuScore = 0
userScore = 0
game = True
while game:
    cpu = random.choice(options)
    user = input("Enter your choice : ")
    print("CPU :",cpu)
    if cpu == user:
        print("Match Tie...")
    elif cpu == "stone"  and user == "paper":
        print("User Win")
        userScore += 1
    elif cpu == "paper" and user == "scissor":
        print("User Win")
        userScore += 1
    elif cpu == "scissor" and user == "stone":
        print("User Win")
        userScore += 1
    elif user == "stone"  and cpu == "paper":
        print("CPU Win")
        cpuScore += 1
    elif user == "paper" and cpu == "scissor":
        print("CPU Win")
        cpuScore += 1
    elif user == "scissor" and cpu == "stone":
        print("CPU Win")
        cpuScore += 1

    print("CPU Score ::",cpuScore)
    print("User Score ::",userScore)

    if userScore == 5 or cpuScore == 5:
        res = "User" if userScore == 5 else "CPU"
        print(res,"Wins...")
        print("Game Over")
        break
