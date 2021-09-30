import random

cpu = random.randint(1,100)
counter = 5
game = True
while game:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("You Win...")
        game = False
        break
    elif cpu > guess:
        print("You have guessed smaller number")
    elif cpu < guess:
        print("You have guessed larger number")
    counter -= 1
    print("Chances Left ::",counter)
    if counter == 0:
        print("You Lose...Number was",cpu)
        game = False