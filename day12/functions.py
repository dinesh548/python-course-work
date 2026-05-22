'''
def greet(name):
    print(f'Hello {name} ,welcome to codegnan')
#name = input("Enter a name: ")
greet("Dinesh")
greet("Nick")
greet("Patrick")

def greet(name):
    print(f'{name} hii macha')
greet('nani')
greet('mani')
-------------------------------------------------------

def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number : {phonenumber}')
    
display('charan','charan@gmail.com','937589458925')
display('charan@gmail.com','charan','937589458925')
----------------------------------------------------------
'''
'''
def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number : {phonenumber}')
    print()
    
display(name='charan',email='charan@gmail.com',phonenumber='937589458925')
display(email='charan@gmail.com',name='charan',phonenumber='937589458925')
-----------------------------------------------------------------------------
'''
'''
def display(name,email,phonenumber=None,cgpa=None):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number : {phonenumber}')
    print(f'cgpa : {cgpa}')
    
display('charan','charan@gmail.com','937589458925',8.06)
display('charan','charan@gmail.com','937589458925')
display('charan','charan@gmail.com')
-----------------------------------------------------
'''
'''
def marks(name,hindi,english,maths):
    print(f'Name : {name}')
    print(f'Hindi : {hindi}')
    print(f'English : {english}')
    print(f'Maths : {maths}')
    print()
marks('charan','80','90','100')
marks('balu','80','90','100')
marks('chari',80,90,100)
-------------------------------------------------------
'''
'''
def display(*names):
    print(names)
display('Nani','mani','chinna')
display('Nani','mani')
display('Nani')
----------------------------------------------
'''
'''
def display(**names):
    print(names)
    print()
display(n1='Nani',n2='mani',n3='chinna')
display(n4='Nani',n5='mani')
display(n6='Nani')
--------------------------------------------
'''
'''
def isprime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
        return True
n=int(input("Enter a number: "))
print('Prime Number' if isprime(n) else "not a prime Number")
---------------------------------------------------------------
'''
































      



























