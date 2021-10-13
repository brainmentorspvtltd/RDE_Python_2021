import random

def game():
    cpu = random.randint(1,100)
    counter = 2
    game = True
    while game:
        guess = int(input("Enter your guess : "))

        if cpu == guess:
            print("Congrats, You guessed the number...")
            game = False
            break
        elif guess > cpu:
            print("You have guessed larger number")
        elif guess < cpu:
            print("You have guessed smaller number")

        counter -= 1
        print("Chances Left ::",counter)
        if counter == 0:
            print("Game Over...Number was",cpu)
            break