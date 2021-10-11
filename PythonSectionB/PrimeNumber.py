num = 17
prime = False
for i in range(2,num//2):
    if num % i == 0:
        # print("Not Prime")
        prime = False
        break
    else:
        # print("Prime")
        prime = True

if prime:
    print("Prime Number")
else:
    print("Not Prime")
