Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=""
s='python'
type(s)
<class 'str'>
s
'python'
a = ''
a
''
a+='language'
a
'language'
id(a)
1420433705968
a='Dinesh'
b='jffrwfjnih'
a+b
'Dineshjffrwfjnih'
a + b
'Dineshjffrwfjnih'
a+b*5
'Dineshjffrwfjnihjffrwfjnihjffrwfjnihjffrwfjnihjffrwfjnih'
a+b*5"\n"
SyntaxError: invalid syntax
"#"*4
'####'
"---*---"*6
'---*------*------*------*------*------*---'
a + b + "---*---"*6
'Dineshjffrwfjnih---*------*------*------*------*------*---'
a + "---*---" b +*6
SyntaxError: invalid syntax
a + "---*---" +b +*6
SyntaxError: invalid syntax
a + "---*---" +b*6
'Dinesh---*---jffrwfjnihjffrwfjnihjffrwfjnihjffrwfjnihjffrwfjnihjffrwfjnih'






















KeyboardInterrupt
a[0]
'D'
a[1:]
'inesh'
a[-1]
'h'
a[-6]
'D'
a[:6]
'Dinesh'
a[-1:]
'h'
a[:-1]
'Dines'
'Dines'
'Dines'
names="John patrick nick mellow"
names
'John patrick nick mellow'
names[start:stop+1:step]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    names[start:stop+1:step]
NameError: name 'start' is not defined
names[:4]
'John'
names[6:13]
'atrick '
names[5:13]
'patrick '
names[-6]
'm'
names[:-6]
'John patrick nick '
names[:-6]
'John patrick nick '
names[-6:]
'mellow'
names[::-1]
'wollem kcin kcirtap nhoJ'
names[-6:-1]
'mello'
names[-1:-6]
''
names[-1:-6:-1]
'wolle'
names[:-6:-1]
'wolle'
names[-12:-19]
''
names[-12:-19:-1]
' kcirta'
names[-11:-19:-1]
'n kcirta'
names[-12:-18:-1]
' kcirt'
names[-12:-20:-1]
' kcirtap'
'dinesh' in names
False
'patrick' in names
True
len(names)
24
sorted(names)
[' ', ' ', ' ', 'J', 'a', 'c', 'c', 'e', 'h', 'i', 'i', 'k', 'k', 'l', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 't', 'w']
ord('a')
97
ord('d')
100
chr(100)
'd'
max(names)
'w'
min(names)
' '
ord(w)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ord(w)
NameError: name 'w' is not defined
ord('w')
119
chr(w)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    chr(w)
NameError: name 'w' is not defined
chr(119)
'w'
names
'John patrick nick mellow'
names.upper
<built-in method upper of str object at 0x0000014AB870D8E0>
names.upper()
'JOHN PATRICK NICK MELLOW'
names.lower()
'john patrick nick mellow'
names.tittle()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    names.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
names.captilize()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    names.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
i='JOHN PATRICK NICK MELLOW'
i.captilize()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    i.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
names.swapcase()
'jOHN PATRICK NICK MELLOW'
l.tittle()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    l.tittle()
NameError: name 'l' is not defined
'jOHN PATRICK NICK MELLOW'.casefold()
'john patrick nick mellow'
names.center(20,'-')
'John patrick nick mellow'
names
'John patrick nick mellow'
names.center(40,'-')
'--------John patrick nick mellow--------'
names.ljust(30,'-')
'John patrick nick mellow------'
names.rjust(30,'-')
'------John patrick nick mellow'
names.center(40,'**')
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    names.center(40,'**')
TypeError: The fill character must be exactly one character long
>>> names.center(40,'*')
'********John patrick nick mellow********'

>>> '5'.2fill(5)
SyntaxError: invalid decimal literal
>>> '5'.zfill(5)
'00005'
>>> '234'.zfill(6)
'000234'
>>> names.rjust(40,'*')
'****************John patrick nick mellow'
>>> names.find(s)
-1
>>> names.find(a)
-1
>>> names.find('a')
6
>>> names.find('z')
-1
>>> names.find('j')
-1
>>> names.find('J')
0
>>> names.find('n')
3
>>> names.rindex('a')
6
>>> names.index('z')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    names.index('z')
ValueError: substring not found
>>> names.count('a')
1
>>> names.count('z')
0
>>> names.count('i')
2
>>> names.replace('a','w')
'John pwtrick nick mellow'
names.replace('i','a')
'John patrack nack mellow'
names.replace("patrick","Dinesh")
'John Dinesh nick mellow'
