Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> x = list()
>>> x = [3,65,7,32,4,8,45.34,"hi"]
>>> type(x)
<class 'list'>
>>> x[0]
3
>>> x[0:4]
[3, 65, 7, 32]
>>> x[::-1]
['hi', 45.34, 8, 4, 32, 7, 65, 3]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append(45)
>>> data
[45]
>>> data.append(37)
>>> data
[45, 37]
>>> data.append(21)
>>> data
[45, 37, 21]
>>> data.append(5,7,7)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data.append(5,7,7)
TypeError: list.append() takes exactly one argument (3 given)
>>> data.append([5,7,7])
>>> data
[45, 37, 21, [5, 7, 7]]
>>> data.pop()
[5, 7, 7]
>>> data
[45, 37, 21]
>>> data.extend([5,7,7])
>>> data
[45, 37, 21, 5, 7, 7]
>>> data + [4,3,6,8]
[45, 37, 21, 5, 7, 7, 4, 3, 6, 8]
>>> data
[45, 37, 21, 5, 7, 7]
>>> data.extend([4,5,6])
>>> data
[45, 37, 21, 5, 7, 7, 4, 5, 6]
>>> data.pop(2)
21
>>> data
[45, 37, 5, 7, 7, 4, 5, 6]
>>> data.insert(2,100)
>>> data
[45, 37, 100, 5, 7, 7, 4, 5, 6]
>>> data.remove(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
>>> data.remove(7)
>>> data
[45, 37, 100, 5, 7, 4, 5, 6]
>>> data.count(5)
2
>>> data.index(5)
3
>>> data.index(5,4)
6
>>> data.sort()
>>> data
[4, 5, 5, 6, 7, 37, 45, 100]
>>> data.sort(reverse=True)
>>> data
[100, 45, 37, 7, 6, 5, 5, 4]
>>> sorted(data)
[4, 5, 5, 6, 7, 37, 45, 100]
>>> data
[100, 45, 37, 7, 6, 5, 5, 4]
>>> data = []
>>> for i in range(1,101):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> data = [i for i in range(1,11)]
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data = [i for i in range(1,51) if i % 2 == 0]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data = [(i,j) for i in range(5) for j in range(4)]
>>> data
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
>>> data = [3,5,7,8,3,4,8]
>>> copy_1 = data
>>> x = 6
>>> y = x
>>> x == y
True
>>> copy_1 == data
True
>>> copy_1 is data
True
>>> data[0]
3
>>> copy_1[0]
3
>>> data
[3, 5, 7, 8, 3, 4, 8]
>>> copy_1
[3, 5, 7, 8, 3, 4, 8]
>>> data[0] = 100
>>> data
[100, 5, 7, 8, 3, 4, 8]
>>> copy_1
[100, 5, 7, 8, 3, 4, 8]
>>> copy_1 = data
>>> copy_2 = data[:]
>>> copy_2 == data
True
>>> copy_2 is data
False
>>> data = [4,5,7,7,23,[4,7,3]]
>>> copy_3 = data[:]
>>> copy_3 is data
False
>>> copy_3 == data
True
>>> data
[4, 5, 7, 7, 23, [4, 7, 3]]
>>> copy_3
[4, 5, 7, 7, 23, [4, 7, 3]]
>>> data[0] = 100
>>> data
[100, 5, 7, 7, 23, [4, 7, 3]]
>>> copy_3
[4, 5, 7, 7, 23, [4, 7, 3]]
>>> data[1][0] = 10
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    data[1][0] = 10
TypeError: 'int' object does not support item assignment
>>> data[-1][0] = 10
>>> data
[100, 5, 7, 7, 23, [10, 7, 3]]
>>> copy_3
[4, 5, 7, 7, 23, [10, 7, 3]]
>>> import copy
>>> copy_4 = copy.deepcopy(data)
>>> x = 10,
>>> x
(10,)
>>> x = 10,20,4,67,7,3
>>> x
(10, 20, 4, 67, 7, 3)
>>> x = (10,20,4,67,7,3)
>>> type(x)
<class 'tuple'>
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = ('Ram',45,45000,'IT)
	
SyntaxError: EOL while scanning string literal
>>> data = ('Ram',45,45000,'IT')
>>> name, age, sal, dept = data
>>> name
'Ram'
>>> age
45
>>> sal
45000
>>> dept
'IT'
>>> 