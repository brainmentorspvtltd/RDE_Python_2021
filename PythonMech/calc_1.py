#Multi-line print
print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice : "))
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

if ch == 1:
    result = num_1 + num_2
elif ch == 2:
    result = num_1 - num_2
elif ch == 3:
    result = num_1 / num_2
elif ch == 4:
    result = num_1 * num_2
else:
    print("Invalid Choice...")

print("Result is",result)
