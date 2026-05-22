'''
n = int(input("Enter a value: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
----------------------------------------

n = int(input("Enter a value: "))
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=" ")
        c+=1
    print()
Enter a value: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
----------------------------------------

n = int(input("Enter a value: "))
for i in range(n):
    for j in range(i+1):
        print(i*j,end=" ")
    print()
Enter a value: 5
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16
----------------------------------------
n = int(input("Enter a value: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
Enter a value: 5
A 
A B 
A B C 
A B C D 
A B C D E
----------------------------------------

l=[12,2,34,55,66,43]
i=0
while i < len(l):
    if l[i]==550:
        print(l[i],'element found:',i)
        break
    i+=1
else:
    print(l[i],'is not element found:',i)
    ----------------------------------------

l=[12,2,34,55,66,43]
i=0
m=0
while i < len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)
   ----------------------------------------

l=[12,2,34,55,66,43,90,55]
i = 0
j=len(l)-1
while i < j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
   ----------------------------------------


#list comprahension
l=[12,2,34,55,66,43,90,55]
res = [i]*l[i] for i in range(len(i))
print(res)
   ----------------------------------------
   
l=[12,2,34,55,66,43,90,55]
res = [i for i in l if i%2==0]
print(res)
----------------------------------------
'''
l=[12,2,34,55,66,43,90,55]
res=[i if i%2 == 0 else 0 for i in l]
print(res)

    





















