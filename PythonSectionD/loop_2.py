# *****
# *****
# *****
# *****
# *****
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

# 1
# 12
# 123
# 1234
# 12345
for i in range(5):
    for j in range(i+1):
        print(j+1, end='')
    print()

# *****
# ****
# ***
# **
# *

# 12345
# 1234
# 123
# 12
# 1

#     *
#    ***
#   *****
#  *******
# *********
for i in range(5):
    for j in range(5-i):
        print(" ", end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

# i = 0, j = 5, k = 1
# -----*
# i = 1, j = 4, k = 3
# ----***
# i = 2, j = 3, k = 5
# ---*****

# 1
# 23
# 456
# 78910
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k, end='')
    print()
