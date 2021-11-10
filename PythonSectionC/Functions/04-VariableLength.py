# *args
def add(*x):
    # print(x)
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    print("Sum is :",sum)

add(4,5)
add(5,6,7,8,8)
add(2,4,6,8,9,5,4,67,8)

def person(**details):
    print(details)

person(name = 'Ram', sal = 45000, dept = 'IT')
person(name = 'Shyam', dept = 'IT', company = 'TCS')


# def edit(*args, **kwargs):
#     pass