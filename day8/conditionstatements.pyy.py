
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
if a==b==c:
    print("Equilateral")
elif a==b and b != c or a==c and b != a:
    print("isosceles")
else:
    print("scalean")

