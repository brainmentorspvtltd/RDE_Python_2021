import random

cpu = random.randint(1,100)

counter = 6
game = True
while game:
    num = int(input("Enter your guess : "))
    if num == cpu:
        print("Congrats, You win...")
        game = False
        break
    elif num > cpu:
        print("You have guessed a larger number")
    elif num < cpu:
        print("You have guessed a smaller number")
    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("You lose..Number was",cpu)
        game = False
