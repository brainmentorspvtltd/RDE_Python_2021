'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

'''
*******
 *****
  ***
   *
'''
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ', end='')
    for k in range(2*i - 1):
        print('*', end='')
    print()

'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
k = 0
for i in range(4):
    for j in range(4-i):
        print(' ', end='')
    for l in range(i+1):
        k = k + 1
        print(k, end=' ')
    print()
