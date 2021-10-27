Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [4,4,1,3,54,76,8,23,67]
>>> x = list()
>>> x = []
>>> x = [4,4,1,3,54,76,8,23,67,'hello',45.55]
>>> type(x)
<class 'list'>
>>> x = [4,4,1,3,54,76,8,23,67]
>>> len(x)
9
>>> x[0]
4
>>> x[0:4]
[4, 4, 1, 3]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> x.append(6)
>>> x
[4, 4, 1, 3, 54, 76, 8, 23, 67, 6]
>>> 