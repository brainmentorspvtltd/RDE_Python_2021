minRange = int(input("Enter a number : "))
maxRange = int(input("Enter a number : "))
for num in range(minRange, maxRange):
    for i in range(2, num):
        if num % i == 0:
            # print("Not Prime")
            break
    else:
        print(num,"is prime")
