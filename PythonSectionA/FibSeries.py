# 0,1,1,2,3,5,8,13,21
a = 1
b = 0

while b < 100:
    print(b, end=',')
    a,b = b,a+b

# a=1,a=0,a=1,a=1,a=2,a=3
# b=0,b=1,b=1,b=2,b=3,b=5
