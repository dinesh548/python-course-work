#12 - 1,2,3,4,6,12
'''
def factors(n):
    res = []
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
def generators(res):
    for i in res:
        yield i
r=factors(38)
g=generators(r)
for i in range(len(r)):
    print(next(g))
---------------------------------

def generators (res):
    for i in range (len (res)-1,-1,-1):
        yield res[i]
1= eval(input("Enter the list: "))
g-generators(1)
for i in range (len(1)):
    print (next(g),end='')
---------------------------------------------------

def even(l):

    return list(filter(lambda i:i%2==0,l))

def gen(l):

    for i in l:

        yield i

l=[1,2,3,4,5,6,7,8,9,10,23,78,90,12,545,5]

e=even(l)

g=gen(e)

for i in range(len(e)):

    print(next(g))
-----------------------------------------------------------------

def fatorial(n):
    if n==1:
        return 1
    return n*fatorial(n-1)
print(fatorial(6))
-----------------------------------------------------------------
'''






























