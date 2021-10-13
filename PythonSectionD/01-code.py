name = input("Enter your name : ")
print("Hello",name)

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = x + y
print("Sum is",z)
print("Sum is %d"%z)
print("Sum of {} and {} is {}".format(x,y,z))

# f-strings = fast / format string literal
print(f"Sum of {x} and {y} is {z}")

