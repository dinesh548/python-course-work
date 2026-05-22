
a=10
float(a)
10.0
complex(a)
(10+0j)
list(a)
#Traceback (most recent call last):
#File "<pyshell#3>", line 1, in <module>
list(a)
#TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=20
b=8.9
int(b)
8
c=10+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+5j)'
bool(c)
True
str(a)
'10'
none(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    none(a)
NameError: name 'none' is not defined. Did you mean: 'None'?
set(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
str="python"
int(str)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'python'
bool(str)
True
list(str)
['p', 'y', 't', 'h', 'o', 'n']
tuple(str)
('p', 'y', 't', 'h', 'o', 'n')
set(str)
{'y', 'p', 'n', 't', 'h', 'o'}
dict(str)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(str)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(str)
True
s="10"
int(s)
10
float(s)
10.0
complex(s)
(10+0j)
li=[1,2,3,4]
int(li)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(li)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
tuple(li)
(1, 2, 3, 4)
set(li)
{1, 2, 3, 4}
dict(li)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(li)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(li)
True
none(li)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    none(li)
NameError: name 'none' is not defined. Did you mean: 'None'?
str(li)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    str(li)
TypeError: 'str' object is not callable
t=(1,2,3,4)
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
bool(t)
True
s={1,2,3,4,5}
int(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
list(s)
[1, 2, 3, 4, 5]
tuple(s)
(1, 2, 3, 4, 5)
d={1:1,2:2,3:3}
int(b)
8
float(d)
SyntaxError: unmatched ')'
float(d)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
list(d)
[1, 2, 3]
str(d)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str(d)
TypeError: 'str' object is not callable
string(d)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    string(d)
NameError: name 'string' is not defined. Did you forget to import 'string'?
bool(d)
True
s=True
int(s)
1
float(s)
1.0
complex(s)
(1+0j)
str(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str(s)
TypeError: 'str' object is not callable
a = 10
b = 20
b = 20.8
c="python"
print(a,b.c)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(a,b.c)
AttributeError: 'float' object has no attribute 'c'
print(a,b,c)
10 20.8 python
print("a",a,"b",b,"c",c)
a 10 b 20.8 c python
a 10 b 20.8 c pythonprint("a",a,"b",b,"c",c)
SyntaxError: invalid syntax
print("a",a,"b",b,"c",c "\n")
SyntaxError: invalid syntax
print("a",a,"b",b,"c",c,sep"")
SyntaxError: invalid syntax
print("a",a,"b",b,"c",c,sep="")
a10b20.cpython
print("a",a,"b",b,"c",c,sep="\n")
a
10
b
20.8
c
python
print("a",a,"b",b,"c",c,"\n")
a 10 b 20.8 c python 

print("a",a,"b",b,"c",c,sep="\t")
a	10	b	20.8	c	python
print("a",a,"b",b,"c",c,sep="@@@")
a@@@10@@@b@@@20.8@@@c@@@python
print("a",a,"b",b,"c",c,sep="\t",end="@@")
a	10	b	20.8	c	python@@
print(f'a: {a},b: {b} c:{c}')
a: 10,b: 20.8 c:python
print('a= %d b=%.2f c=%s'%(a,b,c))
a= 10 b=20.80 c=python
print('a = {} b ={} c= {}'.format(a,bc))
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print('a = {} b ={} c= {}'.format(a,bc))
NameError: name 'bc' is not defined. Did you mean: 'b'?
print('a = {} b ={} c= {}'.format(a,b,c))
a = 10 b =20.8 c= python
print('a = {2} b ={3} c= {1}'.format(a,bc))
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print('a = {2} b ={3} c= {1}'.format(a,bc))
NameError: name 'bc' is not defined. Did you mean: 'b'?
print('a = {2} b ={3} c= {1}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print('a = {2} b ={3} c= {1}'.format(a,b,c))
IndexError: Replacement index 3 out of range for positional args tuple
print('a = {2} b ={0} c= {1}'.format(a,bc))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print('a = {2} b ={0} c= {1}'.format(a,bc))
NameError: name 'bc' is not defined. Did you mean: 'b'?
print('a = {2} b ={0} c= {1}'.format(a,b,c))
a = python b =10 c= 20.8
a=input()
dinesh
a
'dinesh'
name = input("enter a name")
enter a nameDinesh
name
'Dinesh'
type(name)
<class 'str'>
age = input("Enter your age: ")
Enter your age: 21
age
'21'
print(name,age)
Dinesh 21
age = int(input("Enter your age : "))
Enter your age : 22
age
22
age = float(input("enter your age : ")

            23
            
SyntaxError: '(' was never closed
age = float(input("enter your age : "))
            
enter your age : 22
age
            
22.0
"patrick","nick","batman","Ben10".split()
            
('patrick', 'nick', 'batman', ['Ben10'])
age = input("enter ages: ").split()
            
enter ages: 22,33,44,55,66
age
            
['22,33,44,55,66']
age
            
['22,33,44,55,66']
age=list(map(int,input("Enter ages: ").split()))
            
Enter ages: 23,44,556
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    age=list(map(int,input("Enter ages: ").split()))
ValueError: invalid literal for int() with base 10: '23,44,556'
age=(map(float,input("Enter the age: ").split()))
            
Enter the age: 7 5 4
age
...             
<map object at 0x000001F901CE7B20>
>>> list(age)
...             
[7.0, 5.0, 4.0]
>>> names = tuple(input("Enter the Names: ").split())
...             
Enter the Names: dgygyd
>>> names
...             
('dgygyd',)
>>> names = tuple(float("Enter the Names: ").split())
...             
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    names = tuple(float("Enter the Names: ").split())
ValueError: could not convert string to float: 'Enter the Names: '
>>> names = tuple(input("Enter the Names: ").split())
...             
Enter the Names: dgwdgd  jbw sg sss
>>> names
...             
('dgwdgd', 'jbw', 'sg', 'sss')
>>> a = eval(input())
...             
1,2,3
>>> a
...             
(1, 2, 3)
>>> a = eval(input("Enter the dicts: "))
...             
Enter the dicts: 1:2,3:4
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a = eval(input("Enter the dicts: "))
  File "<string>", line 1
    1:2,3:4
     ^
SyntaxError: invalid syntax
