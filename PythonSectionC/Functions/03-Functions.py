# Default Arguments
def calc(x=0,y=0):
    z = x + y
    print("Sum is",z)

# calc()
# calc(5)

# Positional arguments
# calc(4,5)

# Keyword arguments
calc(x=5, y=7)
calc(y=10, x=6)

calc()
calc(5)
calc(6,7)
calc(x=6,y=8)
