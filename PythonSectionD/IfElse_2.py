x = 10
y = 12
z = 23

if x > y and x > z:
    print("X is greater")
elif y > x and y > z:
    print("Y is greater")
else:
    print("Z is greater")

r="X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(r,"is greater")

