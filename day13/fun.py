'''
def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
    print(f'VOWEL : {vc}')
    print(f'CONSONENTS : {cc}')
    print(f'DIGIT : {dc}')
    print(f'word : {wc}')
    print(f'SPECIAL CHARACTER : {sc}')
check("Python Programming : 1233")
--------------------------------------------------
#int,float,str,bool,tuple
#list,set,dict
def display(num):
    num+=5
    print("Inside n :" ,num)
num=10
display(num)
print("outside num :" ,num)
----------------------------------------------------

#call by value/reference
def display():
    global num
    num+=5
    print("Inside n :" ,num)
num=10
display()
print("outside num :" ,num)
----------------------------------------------------

def courses():
    course = "JAVA"
    print("Selected Coures",course)
    def change():
        nonlocal course
        course="PYTHON"
        print("changed",course)
    change()
    print("Final:",course)
courses()
----------------------------------------------------
s="python"
len=5
print(len)
----------------------------------------------------
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)
----------------------------------------------------

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)

s="python"
display(s,0)
----------------------------------------------------


def display(s,ind):
    if ind==len(s):
        return
    
    display(s,ind+1)
    print(s[ind])

s="python"
display(s,0)
----------------------------------------------------

def display(s,ind):
    if ind==len(s)+1:
        return
    print(s[:ind])
    
    display(s,ind+1)
    

s="python"
display(s,1)
----------------------------------------------------
'''
def display(s,ind,w):
    if ind==len(s)-w+1:
        return
    print(s[ind:ind+w])
    display
































    
    

















