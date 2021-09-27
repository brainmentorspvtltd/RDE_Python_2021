# Nested Loop

'''
for i in range(5):
    for j in range(5):
        print(i,j)
'''

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
*****
****
***
**
*
'''




