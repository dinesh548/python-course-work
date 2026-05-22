Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4]
sum(l)
10
any([1,0.0,'',[],(),set(),{},False])
True
all([1,0.0,'',[],(),set(),{},False])
False
all([1,1.1,3,'Dinesh',[1,2,3]])
True
t=()
t=tuple()
t
()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t.add(21)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.add(21)
AttributeError: 'tuple' object has no attribute 'add'
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'python',[1,2,3,4],(2,4,6,8),{5,6,7,8})
t
(1, 1.1, 'python', [1, 2, 3, 4], (2, 4, 6, 8), {8, 5, 6, 7})
t[3]
[1, 2, 3, 4]
t[3].append(12)
t
(1, 1.1, 'python', [1, 2, 3, 4, 12], (2, 4, 6, 8), {8, 5, 6, 7})
a=(1,2,3,4)
x,y,z=a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x,y,z=a
ValueError: too many values to unpack (expected 3)
x
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x
NameError: name 'x' is not defined
a=(1,2,3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,4)
id(t)
2763054703344
t=t+(5,6)
t
(1, 2, 3, 4, 5, 6)
id(t)
2763047773344
t=('Dinesh','Nani','nick','patrick','batman')
t
('Dinesh', 'Nani', 'nick', 'patrick', 'batman')
t+('prince')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t+('prince')
TypeError: can only concatenate tuple (not "str") to tuple
t*5
('Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman')
t(0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t(0)
TypeError: 'tuple' object is not callable
t[0]
'Dinesh'
t[-1]
'batman'
len(t)
5
t[:2]
('Dinesh', 'Nani')
t[:-2]
('Dinesh', 'Nani', 'nick')
t[-2:]
('patrick', 'batman')
t[1::2]
('Nani', 'patrick')
t[-1:-4:-1]
('batman', 'patrick', 'nick')
t
('Dinesh', 'Nani', 'nick', 'patrick', 'batman')
'Dinesh' in t
True
'dinesh' in t
False
'nani' not in t
True
'Nani' in t
True
t+[3]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t+[3]
TypeError: can only concatenate tuple (not "list") to tuple
t+3
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    t+3
TypeError: can only concatenate tuple (not "int") to tuple
t*3
('Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman', 'Dinesh', 'Nani', 'nick', 'patrick', 'batman')
t
('Dinesh', 'Nani', 'nick', 'patrick', 'batman')
t[::-1]
('batman', 'patrick', 'nick', 'Nani', 'Dinesh')
t=(1,1,1,1,1)
t.count(1)
5
t.count(3)
0
t.index(1)
0
t.index(2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t.index(2)
ValueError: tuple.index(x): x not in tuple
max(t)
1
min(t)
1
len(t)
5
sum(t)
5
sorted(t)
[1, 1, 1, 1, 1]
t.sort()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
t.sort
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t.sort
AttributeError: 'tuple' object has no attribute 'sort'
s=[1,2,3,4,5,6,1,2,3,412,22,234]

s
[1, 2, 3, 4, 5, 6, 1, 2, 3, 412, 22, 234]
sorted(s)
[1, 1, 2, 2, 3, 3, 4, 5, 6, 22, 234, 412]
s
[1, 2, 3, 4, 5, 6, 1, 2, 3, 412, 22, 234]
s.sort()
s
[1, 1, 2, 2, 3, 3, 4, 5, 6, 22, 234, 412]
len(s)
12
data={}
type(data)
<class 'dict'>
data{}
SyntaxError: invalid syntax
data
{}
data = {'user id':97,'user_name':'Dinesh','skills':["python",'Java','sql'],'cgpa':8.6}
data
{'user id': 97, 'user_name': 'Dinesh', 'skills': ['python', 'Java', 'sql'], 'cgpa': 8.6}
d={}
d[1]='int'
d[1.1]='float'
d
{1: 'int', 1.1: 'float'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 1.1: 'float', (1, 2, 3, 4): 'tuple'}
d[{1:2,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d[{1:2,2:2}]='dict'
TypeError: unhashable type: 'dict'
d[False]="bool"
d
{1: 'int', 1.1: 'float', (1, 2, 3, 4): 'tuple', False: 'bool'}
data
{'user id': 97, 'user_name': 'Dinesh', 'skills': ['python', 'Java', 'sql'], 'cgpa': 8.6}
data['user id']=102
data
{'user id': 102, 'user_name': 'Dinesh', 'skills': ['python', 'Java', 'sql'], 'cgpa': 8.6}
data['user_name']:'Batman'
data
{'user id': 102, 'user_name': 'Dinesh', 'skills': ['python', 'Java', 'sql'], 'cgpa': 8.6}
data[1]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    data[1]
KeyError: 1
data['user_name']='Batman'
data
{'user id': 102, 'user_name': 'Batman', 'skills': ['python', 'Java', 'sql'], 'cgpa': 8.6}
data['skills']='java'
data
{'user id': 102, 'user_name': 'Batman', 'skills': 'java', 'cgpa': 8.6}
dict={}
type(dict)
<class 'dict'>
'skills' in data
True
data
{'user id': 102, 'user_name': 'Batman', 'skills': 'java', 'cgpa': 8.6}
'age' in data
False
data["skills"]
'java'
data['cgpa']
8.6
data['cpa']
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    data['cpa']
KeyError: 'cpa'
data['age']
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('user_name')
'Batman'
data.get('age')
data
{'user id': 102, 'user_name': 'Batman', 'skills': 'java', 'cgpa': 8.6}
data['user_name']
'Batman'
id(data)
2763053296000
data['user_name']='Dinesh'
id(data)
2763053296000
data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 8.6}
data['cgpa']=10
data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10}
data['cgpa']
10
data['cgap']=9.90
data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9}
data.get('gpa')
>>> data.get('cgpa')
10
>>> data['age']=21
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'age': 21}
>>> data.update({'ph no:xxxxxxxxx','passedout':2026})
SyntaxError: invalid syntax
>>> data.update({'ph no':xxxxxxxxx,'passedout' :2026})
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    data.update({'ph no':xxxxxxxxx,'passedout' :2026})
NameError: name 'xxxxxxxxx' is not defined
>>> data.update({'ph no':983793828783,'passedout':2026})
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'age': 21, 'ph no': 983793828783, 'passedout': 2026}
>>> data['gender']:'male'
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'age': 21, 'ph no': 983793828783, 'passedout': 2026}
>>> data['gender']='male'
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'age': 21, 'ph no': 983793828783, 'passedout': 2026, 'gender': 'male'}
>>> data.pop('age')
21
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'ph no': 983793828783, 'passedout': 2026, 'gender': 'male'}
>>> data.popitem()
('gender', 'male')
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'skills': 'java', 'cgpa': 10, 'cgap': 9.9, 'ph no': 983793828783, 'passedout': 2026}
>>> del data['skills']
>>> data
{'user id': 102, 'user_name': 'Dinesh', 'cgpa': 10, 'cgap': 9.9, 'ph no': 983793828783, 'passedout': 2026}
