Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world this is Python Programming"
>>> type(text)
<class 'str'>
>>> len(text)
38
>>> text[0]
'h'
>>> text[5]
' '
>>> text[7]
'o'
>>> text[10]
'd'
>>> text[-1]
'g'
>>> text = "hello
SyntaxError: EOL while scanning string literal
>>> text = """hello
world
"""
>>> text
'hello\nworld\n'
>>> print(text)
hello
world

>>> text = "hello world this is Python Programming"
>>> text[0:4]
'hell'
>>> text[:]
'hello world this is Python Programming'
>>> text[10:]
'd this is Python Programming'
>>> text[:30]
'hello world this is Python Pro'
>>> text[:100]
'hello world this is Python Programming'
>>> text[5:0]
''
>>> text[5:0:-1]
' olle'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> text[::-1]
'gnimmargorP nohtyP si siht dlrow olleh'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world this is python programming'
>>> text.upper()
'HELLO WORLD THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world this is python programming'
>>> text.title()
'Hello World This Is Python Programming'
>>> text.swapcase()
'HELLO WORLD THIS IS pYTHON pROGRAMMING'
>>> text
'hello world this is Python Programming'
>>> text
'hello world this is Python Programming'
>>> text.replace('i','o')
'hello world thos os Python Programmong'
>>> text
'hello world this is Python Programming'
>>> text[0]
'h'
>>> text[0] = 'y'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    text[0] = 'y'
TypeError: 'str' object does not support item assignment
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text.count('i')
3
>>> text
'hello world this is Python Programming'
>>> text.count('p')
0
>>> text.count('o')
4
>>> text.count('P')
2
>>> text.index('p')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    text.index('p')
ValueError: substring not found
>>> text.index('P')
20
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
24
>>> text.index('o',25)
29
>>> text.index('o',30)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    text.index('o',30)
ValueError: substring not found
>>> text.rindex('o')
29
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
24
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.startswith('a')
False
>>> text.startswith('h')
True
>>> text.endswith('?')
False
>>> text.split()
['hello', 'world', 'this', 'is', 'Python', 'Programming']
>>> #tokenization
>>> text = "    hello     "
>>> text.strip()
'hello'
>>> text.lstrip()
'hello     '
>>> text.rstrip()
'    hello'
>>> text.strip()
'hello'
>>> text.islower()
True
>>> text.isupper()
False
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> 