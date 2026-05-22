Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=['dinesh','nani','nick']
l
['dinesh', 'nani', 'nick']
l.append('babu')
l
['dinesh', 'nani', 'nick', 'babu']
l.insert(1,'nayak')
l
['dinesh', 'nayak', 'nani', 'nick', 'babu']
l.extend(['charan','saniya'])
l
['dinesh', 'nayak', 'nani', 'nick', 'babu', 'charan', 'saniya']
l.remove('saniya')
l
['dinesh', 'nayak', 'nani', 'nick', 'babu', 'charan']
l.pop(p)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l.pop(p)
NameError: name 'p' is not defined
l.pop(1)
'nayak'
l
['dinesh', 'nani', 'nick', 'babu', 'charan']
l.clear()
l
[]
l=['dinesh', 'nani', 'nick', 'babu', 'charan']
sorted(l)
['babu', 'charan', 'dinesh', 'nani', 'nick']
>>> max(l)
'nick'
>>> min(l)
'babu'
>>> len(l)
5
>>> l.index('babu')
3
>>> l.count('dinesh')
1
>>> l
['dinesh', 'nani', 'nick', 'babu', 'charan']
>>> l.sort()
>>> l
['babu', 'charan', 'dinesh', 'nani', 'nick']
>>> l.reverse()
>>> l
['nick', 'nani', 'dinesh', 'charan', 'babu']
>>> l=[1,2,3,4]
>>> m=1
>>> m.append(11)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    m.append(11)
AttributeError: 'int' object has no attribute 'append'
>>> m
1
>>> m=l
>>> m
[1, 2, 3, 4]
>>> m.append(11)
>>> m
[1, 2, 3, 4, 11]
>>> m=n
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    m=n
NameError: name 'n' is not defined
