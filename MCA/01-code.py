a = 6
b = 7
c = a + b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))

print("Sum of {1} and {2} is {0}".format(c,a,b))

#f-strings (fast-strings, format-strings)
print(f"Sum of {a} and {b} is {c}")

#print("1. Add\n2. Sub\n3. Div\n4. Mul")

d = a - b
e = a / b
f = a * b
print(f"""
1. Add is {c}
2. Sub is {d}
3. Div is {e}
4. Mul is {f}
""")








