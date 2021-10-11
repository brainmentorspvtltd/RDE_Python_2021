import random

cpu = random.randint(1,100)
counter = 5
game = True
while game:
    guess = int(input("Enter your guess : "))

    if cpu == guess:
        print("Congrats...You guessed the number")
        game = False
        break
    elif guess < cpu:
        print("You have guessed smaller number")
    elif guess > cpu:
        print("You have guessed larger number")
    counter -= 1
    print("Chances Left :",counter)

    if counter == 0:
        print("Game Over, You Lose...Number was",cpu)
        break