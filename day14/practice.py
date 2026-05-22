'''
n=int(input("Enter a value: "))
for i in range(n):
      for j in range(n-i):
          print(' ',end=" ")
      for k in range(i+1):
          print("*",end=" ")
      print()
---------------------------------------------

l=list(map(int,input().split()))
print(l)
---------------------------------------------------------
products = {
    "salt" : {'stock':40,'discount':10,'price':360},
    'sugar': {'stock':0,'discount':60,'price':304},
    'chilli':{'stock':90,'discount':29,'price':310},
    'bread': {'stock':60,'discount':20,'price':770},
    'honey':{'stock':0,'discount':100,'price':340}
}
for i in products:
    discount=products[i]['discount']
    price=products[i]['price']
    if products[i]['price'] and products[i]['discount']:
        discount=price*discount/100
        price=price-discount
        print(price)
    #print(i,products[i]['stock'])
for i in products:
    if products[i]['stock']:
        price=products[i]['price']
        print(i,price * products[i]['discount']/100)
-----------------------------------------------------------------
#use--->  .split() to convert string to list
a=input("enter a list of string: ").split()
b=tuple(input("enter a list of string: ").split())
c=set(input("enter a list of string: ").split())

#integers to list 
d=list(map(int,input("enter a list of integers: ").split()))
e=tuple(map(int,input("enter a list of integers: ").split()))
f=set(map(int,input("enter a list of integers: ").split())

------------------------------------------------------------------------
'''


























    
