Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [3,5,6,6]
>>> x = []
>>> x = list()
>>> x = [34,56,'hi',56.55]
>>> x = [3,5,6,6]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> x.append(45)
>>> x
[3, 5, 6, 6, 45]
>>> x.append(15)
>>> x
[3, 5, 6, 6, 45, 15]
>>> x.append(15,12,21,5,7,8)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.append(15,12,21,5,7,8)
TypeError: list.append() takes exactly one argument (6 given)
>>> x.append([15,12,21,5,7,8])
>>> x
[3, 5, 6, 6, 45, 15, [15, 12, 21, 5, 7, 8]]
>>> x.pop()
[15, 12, 21, 5, 7, 8]
>>> x
[3, 5, 6, 6, 45, 15]
>>> x.extend([4,3,5,7,8])
>>> x
[3, 5, 6, 6, 45, 15, 4, 3, 5, 7, 8]
>>> x.pop(4)
45
>>> x.insert(4,100)
>>> x
[3, 5, 6, 6, 100, 15, 4, 3, 5, 7, 8]
>>> x.remove(13)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x.remove(13)
ValueError: list.remove(x): x not in list
>>> x.remove(3)
>>> x
[5, 6, 6, 100, 15, 4, 3, 5, 7, 8]
>>> x.index(5)
0
>>> x.index(5,1)
7
>>> x.sort()
>>> x
[3, 4, 5, 5, 6, 6, 7, 8, 15, 100]
>>> x.sort(reverse=True)
>>> x
[100, 15, 8, 7, 6, 6, 5, 5, 4, 3]
>>> sorted(x)
[3, 4, 5, 5, 6, 6, 7, 8, 15, 100]
>>> x
[100, 15, 8, 7, 6, 6, 5, 5, 4, 3]
>>> x = []
>>> for i in range(1,51):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> x = [i for in range(1,11) if i % 2 == 0]
SyntaxError: invalid syntax
>>> x = [i for i in range(1,11) if i % 2 == 0]
>>> x
[2, 4, 6, 8, 10]
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [[i,j] for i in range(1,11) for j in range(5)]
>>> x
[[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4]]
>>> x = [for i in range(1,11) if i % 2 == 0]
SyntaxError: invalid syntax
>>> x
[[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4]]
>>> x = [10,20,22,21,3,57]
>>> for i in range(len(x)):
	print(x[i])

	
10
20
22
21
3
57
>>> for i in x:
	print(i)

	
10
20
22
21
3
57
>>> x = 10,
>>> x = 10,20,3,4,5,7
>>> x = (10,20,3,4,5,7)
>>> x
(10, 20, 3, 4, 5, 7)
>>> x = 10
>>> x
10
>>> x = 10,
>>> x
(10,)
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> x[0] = 10
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    x[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> data = {"name" : "Ram", "age" : 18, "college" : "RD"}
>>> type(data)
<class 'dict'>
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ram'
>>> data['college']
'RD'
>>> data['age']
18
>>> data['name'] = 'Shyam'
>>> data
{'name': 'Shyam', 'age': 18, 'college': 'RD'}
>>> data['marks'] = 78
>>> data
{'name': 'Shyam', 'age': 18, 'college': 'RD', 'marks': 78}
>>> data['subject'] = ["phy","math","python"]
>>> data
{'name': 'Shyam', 'age': 18, 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python']}
>>> data["details"] = {"address" : "Delhi", "ph" : 54454545}
>>> data
{'name': 'Shyam', 'age': 18, 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python'], 'details': {'address': 'Delhi', 'ph': 54454545}}
>>> data["subjects"]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    data["subjects"]
KeyError: 'subjects'
>>> data["subject"]
['phy', 'math', 'python']
>>> data["details"]
{'address': 'Delhi', 'ph': 54454545}
>>> data["details"]["address"]
'Delhi'
>>> data.pop("age")
18
>>> data
{'name': 'Shyam', 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python'], 'details': {'address': 'Delhi', 'ph': 54454545}}
>>> data.popitem()
('details', {'address': 'Delhi', 'ph': 54454545})
>>> data
{'name': 'Shyam', 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python']}
>>> details = {'address': 'Delhi', 'ph': 54454545}
>>> data.update(details)
>>> data
{'name': 'Shyam', 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python'], 'address': 'Delhi', 'ph': 54454545}
>>> data.get('name')
'Shyam'
>>> data.get('marks')
78
>>> data['name']
'Shyam'
>>> data['marks']
78
>>> data['age']
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('age')
>>> data.get('age', 'Invalid Key')
'Invalid Key'
>>> data.get('name', 'Invalid Key')
'Shyam'
>>> data.get('nam', 'Invalid Key')
'Invalid Key'
>>> data
{'name': 'Shyam', 'college': 'RD', 'marks': 78, 'subject': ['phy', 'math', 'python'], 'address': 'Delhi', 'ph': 54454545}
>>> for item in data:
	print(item)

	
name
college
marks
subject
address
ph
>>> data.keys()
dict_keys(['name', 'college', 'marks', 'subject', 'address', 'ph'])
>>> data.values()
dict_values(['Shyam', 'RD', 78, ['phy', 'math', 'python'], 'Delhi', 54454545])
>>> for item in data.values():
	print(item)

	
Shyam
RD
78
['phy', 'math', 'python']
Delhi
54454545
>>> data.items()
dict_items([('name', 'Shyam'), ('college', 'RD'), ('marks', 78), ('subject', ['phy', 'math', 'python']), ('address', 'Delhi'), ('ph', 54454545)])
>>> for item in data.items():
	print(item)

	
('name', 'Shyam')
('college', 'RD')
('marks', 78)
('subject', ['phy', 'math', 'python'])
('address', 'Delhi')
('ph', 54454545)
>>> for item in data:
	print(item)

	
name
college
marks
subject
address
ph
>>> for item in data:
	print(data[item])

	
Shyam
RD
78
['phy', 'math', 'python']
Delhi
54454545
>>> for item in data:
	print(item, data[item])

	
name Shyam
college RD
marks 78
subject ['phy', 'math', 'python']
address Delhi
ph 54454545
>>> data["subject"]
['phy', 'math', 'python']
>>> data["subject"][0]
'phy'
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionC/dict_exercise.py
Mohit 65
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionC/dict_exercise.py
Enter Student Name : Amit
89
>>> 