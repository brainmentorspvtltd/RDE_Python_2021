x,y,z = 10,23,3

if x > y and x > z:
    print("X is greatest")
elif y > x and y > z:
    print("Y is greatest")
else:
    print("Z is greatest")

r="X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(r,"is greatest")

