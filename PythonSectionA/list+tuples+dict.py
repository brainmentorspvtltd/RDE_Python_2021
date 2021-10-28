Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> type(x)
<class 'list'>
>>> x = [4,5,6,3,'hi']
>>> x = [4,3,6]
>>> x.append(12)
>>> x
[4, 3, 6, 12]
>>> x.pop()
12
>>> x
[4, 3, 6]
>>> x.append(45,2,5,7,78)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.append(45,2,5,7,78)
TypeError: list.append() takes exactly one argument (5 given)
>>> x.append([45,2,5,7,78])
>>> x
[4, 3, 6, [45, 2, 5, 7, 78]]
>>> x.pop()
[45, 2, 5, 7, 78]
>>> x
[4, 3, 6]
>>> x.extend([45,2,5,7,78])
>>> x
[4, 3, 6, 45, 2, 5, 7, 78]
>>> x.pop()
78
>>> x.pop(5)
5
>>> x
[4, 3, 6, 45, 2, 7]
>>> x.remove(10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x.remove(10)
ValueError: list.remove(x): x not in list
>>> x.remove(3)
>>> x
[4, 6, 45, 2, 7]
>>> x.count(2)
1
>>> x.index(2)
3
>>> x.insert(3,100)
>>> x
[4, 6, 45, 100, 2, 7]
>>> x.sort()
>>> x
[2, 4, 6, 7, 45, 100]
>>> x.sort(reverse=True)
>>> x
[100, 45, 7, 6, 4, 2]
>>> x.reverse()
>>> x
[2, 4, 6, 7, 45, 100]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a,b = 10,20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> x = []
>>> for i in range(1,51):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> x = [for i in range(10)]
SyntaxError: invalid syntax
>>> x = [i for i in range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = [i for i in range(1,11) if i % 2 == 0]
>>> x
[2, 4, 6, 8, 10]
>>> x = [i ** 2 for i in range(1,11)]
>>> x
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> x = [[i,j] for i in range(5) for j in range(5) if i == j]
>>> x
[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
>>> x = [4,5,7,8,3]
>>> y = x
>>> x
[4, 5, 7, 8, 3]
>>> y
[4, 5, 7, 8, 3]
>>> x == y
True
>>> y[0] = 100
>>> y
[100, 5, 7, 8, 3]
>>> x
[100, 5, 7, 8, 3]
>>> x is y
True
>>> z = x.copy()
>>> x
[100, 5, 7, 8, 3]
>>> y
[100, 5, 7, 8, 3]
>>> z
[100, 5, 7, 8, 3]
>>> x == z
True
>>> x
[100, 5, 7, 8, 3]
>>> z
[100, 5, 7, 8, 3]
>>> x is z
False
>>> id(x)
2551799914752
>>> id(y)
2551799914752
>>> id(z)
2551799851968
>>> y = x
>>> x = [4,56,7,7,3,[4,6,7,98,2]]
>>> y = x.copy()
>>> x
[4, 56, 7, 7, 3, [4, 6, 7, 98, 2]]
>>> y
[4, 56, 7, 7, 3, [4, 6, 7, 98, 2]]
>>> x == y
True
>>> x is y
False
>>> x[0] = 400
>>> x
[400, 56, 7, 7, 3, [4, 6, 7, 98, 2]]
>>> y
[4, 56, 7, 7, 3, [4, 6, 7, 98, 2]]
>>> x[-1][0]
4
>>> x[-1][0] = 50
>>> x
[400, 56, 7, 7, 3, [50, 6, 7, 98, 2]]
>>> y
[4, 56, 7, 7, 3, [50, 6, 7, 98, 2]]
>>> import copy
>>> z = copy.deepcopy(x)
>>> x
[400, 56, 7, 7, 3, [50, 6, 7, 98, 2]]
>>> z
[400, 56, 7, 7, 3, [50, 6, 7, 98, 2]]
>>> x[-1][0] = 500
>>> x
[400, 56, 7, 7, 3, [500, 6, 7, 98, 2]]
>>> y
[4, 56, 7, 7, 3, [500, 6, 7, 98, 2]]
>>> z
[400, 56, 7, 7, 3, [50, 6, 7, 98, 2]]
>>> x = 10
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x = 10,20,40
>>> x = (10,20,40)
>>> x
(10, 20, 40)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> data = ("Ram","dept",45000)
>>> name, dept, sal = data
>>> name
'Ram'
>>> dept
'dept'
>>> sal
45000
>>> data
('Ram', 'dept', 45000)
>>> name, dept = data
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    name, dept = data
ValueError: too many values to unpack (expected 2)
>>> name, *details = data
>>> name
'Ram'
>>> details
['dept', 45000]
>>> data = {"name" : "Ram", "dept" : "IT", "sal" : 45000}
>>> data
{'name': 'Ram', 'dept': 'IT', 'sal': 45000}
>>> type(data)
<class 'dict'>
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["name"]
'Ram'
>>> data["dept"]
'IT'
>>> data["sal"]
45000
>>> data.keys()
dict_keys(['name', 'dept', 'sal'])
>>> data.values()
dict_values(['Ram', 'IT', 45000])
>>> data.items()
dict_items([('name', 'Ram'), ('dept', 'IT'), ('sal', 45000)])
>>> data.get("name")
'Ram'
>>> data["name"]
'Ram'
>>> data["address"]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    data["address"]
KeyError: 'address'
>>> data.get("address")
>>> data.get("address", "Data Not Available")
'Data Not Available'
>>> data.get("name", "Data Not Available")
'Ram'
>>> details = {"address":"Delhi", "ph" : 565698778}
>>> data.update(details)
>>> data
{'name': 'Ram', 'dept': 'IT', 'sal': 45000, 'address': 'Delhi', 'ph': 565698778}
>>> data["company"] = "TCS"
>>> data
{'name': 'Ram', 'dept': 'IT', 'sal': 45000, 'address': 'Delhi', 'ph': 565698778, 'company': 'TCS'}
>>> data.pop()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.pop("sal")
45000
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': 'Delhi', 'ph': 565698778, 'company': 'TCS'}
>>> data.popitem()
('company', 'TCS')
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': 'Delhi', 'ph': 565698778}
>>> for item in data:
	print(item)

	
name
dept
address
ph
>>> for item in data.values():
	print(item)

	
Ram
IT
Delhi
565698778
>>> for item in data:
	print(item, data[item])

	
name Ram
dept IT
address Delhi
ph 565698778
>>> for i in range(len(x)):
	print(x[i])

	
10
20
40
>>> x
(10, 20, 40)
>>> for i in x:
	print(i)

	
10
20
40
>>> data = {
    "names" : ["Ram","Shyam","Amit","Mohit","Naman"],
    "marks" : [67,87,76,33,89],
    "branch" : ["IT","CS","CS","EC","EC"]
    }
>>> 
>>> data["names"]
['Ram', 'Shyam', 'Amit', 'Mohit', 'Naman']
>>> data["names"][0]
'Ram'
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionA/dict_exercise_1.py
Enter Student Name : Ram
67
>>> 