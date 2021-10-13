# 0,1,1,2,3,5,8,13,21....
num = int(input("Enter the number : "))
a = 1
b = 0
# while b < 100:
#     print(b)
#     a,b = b,a+b

for i in range(num):
    print(b, end=', ')
    a, b = b, a + b

# a=1, a=0, a=1, a=1, a=2
# b=0, b=1, b=1, b=2, b=3
#
# 0,1,1,2,3