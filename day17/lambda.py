#l=[1,22,3,4,5,6,7,8,567,334,257]
'''
l='python programming language'
res = list(filter(lambda i:i in 'aeiouAEIOU',l))
print(res)

s='hbwubywbfyurrfbrwhfbhrbf'
res=list(filter(lambda i:i in "aeiouAEIOU",s))
print(res)
----------------------------------------------------------------

l=['operators','control','conditional','oops','files','exception']
res = list(filter(lambda i:i[0] not in 'aeiouAEIOU',l))
print(res)
---------------------------------------------------------------

data = {
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':55000},
    'mac':{'stock':35,'price':95000},
    'hp':{'stock':25,'price':65000},
    'asus':{'stock':0,'price':35000}
   }

res=list(filter(lambda i:data[i]['stock']==0,data))
print(res)
res=list(filter(lambda i:data[i]['price']>50000,data))
print(res)
-----------------------------------------------------

data = {
    'dell':{'stock':0,'price':89000},
    'lenova':{'stock':15,'price':55000},
    'mac':{'stock':35,'price':95000},
    'hp':{'stock':25,'price':65000},
    'asus':{'stock':0,'price':35000}
   }
res={i:data[i]['price'] for i in data}
l2h=sorted(res.items(),key=lambda i:i[1])
h2l=sorted(res.items(),key=lambda i:i[1],reverse=True)
print('low to high: ')
print(l2h)
print()
print('high to low: ')
print(h2l)
--------------------------------------------------------------

from functools import reduce
l=[1,2,3,3,4,5,6,7,66,89]
m=['operators','control','conditional','oops','files','exception']
ms=reduce(lambda sum,i:sum+','+i,m)
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p,ms)
--------------------------------------------------------------

#generators

def reels():
    r=['1..100','101..200','201..300','301..400','401..500','501..600']
    for i in r:
       yield i
scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
--------------------------------------------------------------
'''
def reels():
    return '1-10 files'
    return '11-20 files'
    return '21-30 files'
    return '31-40 files'
    return '41-50 files'
scroll=reels()
print(scroll)

























