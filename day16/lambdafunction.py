'''
check = lambda num:"even" if num%2==0 else "odd"
print(check(10))
print(check(1023))
print(check(1033334))
--------------------------------------------------

square = lambda num:num**2
print(square(10))
print(square(1023))
print(square(1033334))

cube = lambda num : num**3
print(cube(12))
--------------------------------------------------

check=lambda a,b: a if a>b else b
print(check(121,113))
--------------------------------------------------
check = lambda s:len(s)
print(check("ibbhbvhbhbhb"))
print(check("12345"))
--------------------------------------------------

a="aeiouAEIOU"
check = lambda s:"start with vowel" if s[0] in a else "start with consonant"
print(check("Dinesh"))
print(check("Abhi"))
--------------------------------------------------

check = lambda s:"start with vowel" if s[0] in "aeiouAEIOU" else "start with consonant"
print(check("Dinesh"))
print(check("Abhi"))
--------------------------------------------------

check=lambda email:email.split('@')[-1]
print(check('abc@gmail.com'))
print(check('abc@codegnan.com'))
print(check('abc@yahooo.com'))
--------------------------------------------------

check = lambda year:'leap year' if year % 400 == 0 or (year % 4==0 and year%100!=0) else 'Not a leap year'
print(check(2024))
--------------------------------------------------

l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**2,l))
print(res)
--------------------------------------------------

l=['hello','python']
res=list(map(lambda i:i.upper(),l))
print(res)
--------------------------------------------------
'''
l={'Dinesh':90,'John':79,'patrick':69,'nick':89}
print(dict(sorted(l.items(),key=lambda i:i[1])))
print(dict(sorted(l.items(),key=lambda i:i[1],reverse=True)))
























