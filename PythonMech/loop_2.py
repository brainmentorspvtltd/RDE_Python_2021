'''
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                print(i,j,k,l)
            print("*"*20)
        print("*"*20)
    print("*"*20)
print("*"*20)
'''

'''
  01234
0 *****
1 *****
2 *****
3 *****
4 *****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

'''
  01234
0 *
1 **
2 ***
3 ****
4 *****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

'''
  01234
0 1
1 12
2 123
3 1234
4 12345
'''
for i in range(5):
    for j in range(i+1):
        print(j+1, end='')
    print()


'''
  01234
0 1
1 22
2 333
3 4444
4 55555
'''
for i in range(5):
    for j in range(i+1):
        print(i+1, end='')
    print()
