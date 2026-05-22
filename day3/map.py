Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a/b
0.5
a//b
0
a%b
10
10/3
3.3333333333333335
14%3
2
2**3
8
8**2
64
3**3
27
a==b
False
a!b
SyntaxError: invalid syntax
a!+b
SyntaxError: invalid syntax
a!=b
True
a<b
True
a>b
False
a<=b
True
a>=b
False
#assignment operators
a=40
a=a+10
a
50
a=a+20
a
70
a+=10
a
80
a-=30
a
50
a*=2
a
100
a//=30
a
3
a**=3
a
27
a/=2
a
13.5
#logical
a=6
a%2==0 and a%3==0 and a%6==0
True
a=12
a%2==0 and a%3==0 and a%6==0
True
a=32
a%2==0 or a%3==0 or a%6==0
True
not a
False
not b
False
not 3
False
not a%2==0
False
not a%2!=0
True
#str,list,tuple,set,dict
"p" in python
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    "p" in python
NameError: name 'python' is not defined
"p" in "python"
True
l = [1,2,3,4]
2 in l
True
9 in l
False
9 not in l
True
2 not in l
False
s=(1,2,3,4,5)
2 in s
True
9 not in s
True
True
True
d = [1:2,2:3,3:4]
SyntaxError: invalid syntax
d = (1:2,2:3,3:4)
SyntaxError: invalid syntax
d = {1:2,2:3,3:4}
4 in d
False
d.keywords
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.keywords
AttributeError: 'dict' object has no attribute 'keywords'
d.keys
<built-in method keys of dict object at 0x000001F565F1F280>
print(d.keys())
dict_keys([1, 2, 3])
#idendity
a = [1,2,3,4]
b = [1,2,3,4]
a==b
True
a is b
False
 c=a
 
SyntaxError: unexpected indent
c=a
c
[1, 2, 3, 4]
a is c
True
id(c)
2153488754176
id(a)
2153488754176
a is c
True
a is not c
False
id(b)
2153438027776
a is b
False
a is not b
True
id(e)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    id(e)
NameError: name 'e' is not defined
d = []
id(d)
2153489062592
e = []
d is e
False
id(e)
2153488996352
f = e
f is e
True
id(f)
2153488996352
id(e)
2153488996352
#Binary numbers
0: 00001: 00012: 00103: 00114: 01005: 01016: 01107: 01118: 10009: 100110: 101011: 101112: 110013: 110114: 111015: 1111
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 0: 0000
... 1: 0001
... 2: 0010
... 3: 0011
... 4: 0100
... 5: 0101
... 6: 0110
... 7: 0111
... 8: 1000
... 9: 1001
... 10: 1010
... 11: 1011
... 12: 1100
... 13: 1101
... 14: 1110
... 15: 1111
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 10 & 11
10
>>> 7 & 13
5
>>> 7 ! 13
SyntaxError: invalid syntax
>>> 7 | 13
15
>>> 8<<1
16
>>> 8>>1
4
>>> 8^5
13
>>> 1^3
2
>>> 1^1
0
>>> 5^4
1
