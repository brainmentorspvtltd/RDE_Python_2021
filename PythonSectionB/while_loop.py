a = 0
while a < 10:
    print(a, end=',')
    a += 1

print()

a = 0
while True:
    print(a,end=',')
    a += 1
    if a == 10:
        break

print()

a = 0
flag = True
while flag:
    print(a,end=',')
    a += 1
    if a == 10:
        flag = False