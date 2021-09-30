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

