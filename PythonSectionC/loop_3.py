#Nested Loop
for i in range(5):
    for j in range(5):
        print(i,j)
    print('=' * 10)
'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()


'''
a
bb
ccc
dddd
eeeee
'''
for i in range(5):
    for j in range(i+1):
        print(chr(97+i), end='')
    print()

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')
    print()

'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k = k + 1
        print(k, end='')
    print()

