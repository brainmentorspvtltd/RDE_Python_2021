num = 17
for i in range(2,num//2):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
