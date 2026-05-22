'''
n=int(input('Enter a size: '))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
------------------------------------
n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * *
-----------------------------------

n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
* * * * * 
* * * * 
* * * 
* * 
*
-----------------------------------
n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
--------------------------------------

n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
         print('*',end=' ')     
    print()
* * * * * 
  * * * * 
    * * * 
      * * 
        *
-------------------------------------------
n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(n):
        if j%2==0:
            print('0',end=' ')
        else:
            print('1',end=' ')      
    print()
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0
--------------------------------------------
n=int(input('Enter a size: '))               
for i in range(n):
    for j in range(n):
        
        print(int((i+j)%2==0),end=' ')
              
    print()
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1
------------------------------------------
n=int(input('Enter a size: '))
for i in range(n):
    for j in range(n):
        if i == 0 or i == (n-1) or j==0 or j==(n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
----------------------------------------------       
n=int(input('Enter a size: '))
for i in range(n):
    for j in range(n):
        if i == 0 or i == (n-1) or j==0 or j==(n-1)or n//2==i or n//2==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
----------------------------------------------


n=int(input('Enter a size: '))

for i in range(n):
    for j in range(n):

        if i == 0 or i == n-1 or i + j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()
* * * * * 
      *   
    *     
  *       
* * * * *
-----------------------------------------

n=int(input('Enter a size: '))

for i in range(n):
    for j in range(n):

        if  i + j == n-1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()
    
*       * 
  *   *   
    *     
  *   *   
*       * 
-----------------------------------------
'''
n=int(input('Enter a size: '))

for i in range(n):
    for j in range(n):

        if  i==0 or j==0 or(i==(n-1) and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>=n//2) or (j==n-1 or j>=n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()






