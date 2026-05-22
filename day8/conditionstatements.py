'''
data={
    'dinesh@gmail.com':'nima@123',
    'babu@gmail.com':'ch@123'
    }
email=input("Enter a email: ")
password=input("Enter a password: ")
if data.get(email):
    print("Login successful")
else:
    print("login invalid")
---------------------------------------------------  

import random
otp=random.randint(1111,9999)
print("your otp",otp)
entered_otp=int(input("Enter otp: "))
if otp == entered_otp:
    print("verified successfully")
else:
    print("invalid")

hr,min = list(map(int,input("Enter the time(hh:min): ").split(':')))
fare = 0
price =100
if 0<hr<23 and 0<=min<=59:
    
    if 8<=hr<16:
        fare = 40
    elif 16<=hr<23:
        fare = 100
    elif 0<=hr<=7:
        fare = 150
    print("Total fare",fare+price)
else:
    print("Invalid time")
'''     

data = {
    'Dinesh':{'status':True,'python':50,'mysql':70,'flask':89},
    'balu':{'status':True,'python':90,'mysql':30,'flask':79},
    'nick':{'status':False,'python':None,'mysql':None,'flask':None},
    'james':{'status':True,'python':40,'mysql':90,'flask':80},
    'patrick':{'status':False,'python':70,'mysql':60,'flask':89},
    }
name = input("Enter a name: ")
if name in data:
    print(name,'s, report')
    if data[name]['status']:
        avg=data[name]['python']+data[name]['mysql']+data[name]['flask']/3
        if 
        
    else:
        print(name,"didn't attend the exam")
else:
    print("not found")
    































