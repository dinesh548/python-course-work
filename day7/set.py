Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=()
type(s)
<class 'tuple'>
d={1:2}
type(d)
<class 'dict'>
d={}
type(d)
<class 'dict'>
d={9}
type(d)
<class 'set'>
d={1:2,2:3,3:7,4:9,6:36}
d.keys{}
SyntaxError: invalid syntax
d.keys()
dict_keys([1, 2, 3, 4, 6])
d.values()
dict_values([2, 3, 7, 9, 36])
d.item()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
d.items()
dict_items([(1, 2), (2, 3), (3, 7), (4, 9), (6, 36)])
len(d)
5
max(d)
6
min(d)
1
d
{1: 2, 2: 3, 3: 7, 4: 9, 6: 36}
d(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d(1)
TypeError: 'dict' object is not callable
sorted(d)
[1, 2, 3, 4, 6]
d.get(6)
36
s=set()
s
set()
s={1,4,3,66,4,666,2,53}
type(s)
<class 'set'>
s
{1, 2, 3, 4, 66, 53, 666}
s=set()
s.add(1)
s
{1}
s.add{1.2}
SyntaxError: invalid syntax
s.add(1.2)
s
{1, 1.2}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,23,4))
s
{1, (1, 23, 4), 1.2}
s.add(4+3j)

s
{(4+3j), 1, (1, 23, 4), 1.2}
s.add(False)
s
{False, 1, 1.2, (1, 23, 4), (4+3j)}
s.add({1:2})
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s.add({1:2})
TypeError: unhashable type: 'dict'
s
{False, 1, 1.2, (1, 23, 4), (4+3j)}
s.add('string')
s
{False, 1, 1.2, (1, 23, 4), (4+3j), 'string'}
1 in s
True
2 in s
False
1.1 in s
False
1.2 in s
True
a={1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
b={2,3,4,5,6,7,8,9,10}
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a & b
{2, 3, 4, 5, 6}
a - b
{1}
b - a
{8, 9, 10, 7}
a ^ b
{1, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6}
{1,2}<a
True
{1,2,10,3}<a
False
{1,2,3,4,5,6}>a
False
a<b
False
a>b
False
x={1,2}
y={3,4}
x.disjoint(y)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    x.disjoint(y)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
x.isdisjoint(y)
True
a
{1, 2, 3, 4, 5, 6}
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersetion(b)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.intersetion(b)
AttributeError: 'set' object has no attribute 'intersetion'. Did you mean: 'intersection'?
a.intersection(b)
{2, 3, 4, 5, 6}
a.differece(b)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.differece(b)
AttributeError: 'set' object has no attribute 'differece'. Did you mean: 'difference'?
a.difference(b)
{1}
a.symmetric difference(b)
SyntaxError: invalid syntax
a ^ b
{1, 7, 8, 9, 10}
a.subset(b)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.subset(b)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
a.issubset(b)
False
a.issuperset(b)
False
sorted(a)
[1, 2, 3, 4, 5, 6]
max(a)
6
min(a)
1
len(a)
6
sum(a)
21
a.add(80)
a
{80, 1, 2, 3, 4, 5, 6}
a.update({88,99,100})
a
{1, 2, 3, 4, 5, 6, 99, 100, 80, 88}
a.pop(100)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.pop(100)
TypeError: set.pop() takes no arguments (1 given)
a.pop()
1
a
{2, 3, 4, 5, 6, 99, 100, 80, 88}
a.pop()
2
a
{3, 4, 5, 6, 99, 100, 80, 88}
a.clear()
a
set()
a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.del(5)
SyntaxError: invalid syntax
a.remove(5)
a
{1, 2, 3, 4, 6, 7, 8, 9, 10}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a.remove(10)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a.discard(999)
>>> a.discard(3)
>>> a
{1, 2, 4, 5, 6, 7, 8, 9}
>>> {1, 2, 4, 5, 6, 7, 8, 9}
{1, 2, 4, 5, 6, 7, 8, 9}
>>> c=b
>>> c.add(1000)
>>> c
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000}
>>> b
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000}
>>> d=b.copy
>>> d
<built-in method copy of set object at 0x0000012A47218E40>
>>> d=b.copy()
>>> d
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000}
>>> d.add(12345)
>>> d
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000, 12345}
>>> b
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000}
>>> a.intersection(b)
{2, 4, 5, 6, 7, 8, 9}
>>> a.intersection_update(b)
>>> a
{2, 4, 5, 6, 7, 8, 9}
>>> b
{2, 3, 4, 5, 6, 7, 8, 9, 10, 1000}
>>> a
{2, 4, 5, 6, 7, 8, 9}
