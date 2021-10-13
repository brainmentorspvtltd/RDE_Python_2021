import random
options = ["stone", "paper", "scissor"]
userScore = 0
cpuScore = 0
while True:
    cpu = random.choice(options)
    user = input("Enter your choice : ")
    print("CPU ::",cpu)
    if user == cpu:
        print("Match Draw")
    elif user == "stone" and cpu == "scissor":
        print("User Win")
    elif user == "paper" and cpu == "stone":
        print("User Win")
    elif user == "scissor" and cpu == "paper":
        print("User Win")
    elif user == "stone" and cpu == "paper":
        print("CPU Win")
    elif user == "paper" and cpu == "scissor":
        print("CPU Win")
    elif user == "scissor" and cpu == "stone":
        print("CPU Win")
