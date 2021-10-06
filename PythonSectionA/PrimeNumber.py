num = int(input("Enter a number : "))

prime = False

for i in range(2,num):
    if num % i == 0:
        # print("Not Prime")
        prime = False
        break
    else:
        # print("Prime")
        prime = True

if prime:
    print(num,"is a prime number")
else:
    print(num,"is not prime")
