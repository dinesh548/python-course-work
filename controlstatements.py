#init
#while cond:
    #update
'''
l=[1,2,3,0,2,3,0,4,5]
while 0 in l:
    l.remove(0)
print(l)

i=1
while i<=10:
    print(i)
    i+=1

i = 100
while i>=2:
    print(i)
    i-=2

n=int(input("enter a value: "))
i=1
while i<=10:
    print(f'{n}x{i} = {n*i}')
    i+=1

i=1
while i<=10:
    i+=1
    if i==5:
        break
    print(i)

n = int(input("Enter a value: "))
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)

n = int(input("Enter a value: "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)

n = int(input("Enter a value: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
   

n = input("Enter a string: ")
res=''
for i in n:
    res+=chr(ord(i)+1)
print(res)

n = input("Enter a string: ")
i=len(n)-1
while i>=0:
    print(n[i],i)
    i-=1

#non repeating
n = input("Enter a string: ")
for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("all repeating mul times")
        
'''
n = int(input("Enter a value: "))
res = 0
while n>=0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)
    

        
    
        























