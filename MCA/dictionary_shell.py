Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [12,10,34,22,67,34]
>>> x = (12,10,34,22,67,34)
>>> age = [12,10,34,22,67,34]
>>> data = {'name':'John', '}
	
SyntaxError: EOL while scanning string literal
>>> data = {'name':'John', 'rollno':45,'branch':'IT'}
>>> data.keys()
dict_keys(['name', 'rollno', 'branch'])
>>> data.values()
dict_values(['John', 45, 'IT'])
>>> data.items()
dict_items([('name', 'John'), ('rollno', 45), ('branch', 'IT')])
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'John'
>>> data['rollno']
45
>>> data['branch']
'IT'
>>> data['address'] = "delhi"
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT', 'address': 'delhi'}
>>> data.get('name')
'John'
>>> data['name']
'John'
>>> data['mobile']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data['mobile']
KeyError: 'mobile'
>>> data.get('mobile')
>>> data.get('mobile','Not available')
'Not available'
>>> data.get('name','Not available')
'John'
>>> data.pop()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.pop('address')
'delhi'
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT'}
>>> details = {'address':'delhi','phone':'9898988888'}
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT'}
>>> details
{'address': 'delhi', 'phone': '9898988888'}
>>> data.update(details)
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT', 'address': 'delhi', 'phone': '9898988888'}
>>> data.popitem()
('phone', '9898988888')
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT', 'address': 'delhi'}
>>> data.setdefault('phone')
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT', 'address': 'delhi', 'phone': None}
>>> data.popitem()
('phone', None)
>>> data.setdefault('phone',89898989)
89898989
>>> data
{'name': 'John', 'rollno': 45, 'branch': 'IT', 'address': 'delhi', 'phone': 89898989}
>>> for key in data:
	print(key)

	
name
rollno
branch
address
phone
>>> for key in data:
	print(data[key])

	
John
45
IT
delhi
89898989
>>> for key in data:
	print(key,"-",data[key])

	
name - John
rollno - 45
branch - IT
address - delhi
phone - 89898989
>>> for val in data.values():
	print(val)

	
John
45
IT
delhi
89898989
>>> x
(12, 10, 34, 22, 67, 34)
>>> x[0]
12
>>> for i in range(len(x)):
	print(i)

	
0
1
2
3
4
5
>>> for i in range(len(x)):
	print(x[i])

	
12
10
34
22
67
34
>>> for i in x:
	print(i)

	
12
10
34
22
67
34
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise.py
Enter name of student : John
78
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise.py
Enter name of student : Nick
79
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise.py
224 3
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise.py
74.66666666666667
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise_2.py
Enter student name : Aman
119
>>> 
= RESTART: D:/Trainings/RDE_Python_2021-main/PythonSectionB/dictionary_exercise_2.py
Enter student name : Aman
119
>>> 