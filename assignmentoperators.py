"""assignment operators are
   =
   +=
   -=
   *=
   /=
   %=
   **=
   //=     """

p=q=r=22
print(p,q,r)   #o/p = 22 22 22

a,b=10,5
   
b=a
print(b)  #o/p = 10 ,here a value is assigned to b

a+=b
print(a)  #o/p =20 because in b is already 10 so 10+10=20

a-=b
print(a)  #o/p=10

a*=b
print(a)  #o/p = 100

a/=b
print(a)  #o/p = 10.0 because 100/10=10.0

a=b=2
a**=b
print(a)  #o/p = 4 that is 2 pow 2 = 4

a,b=100,10
a//=b
print(a)  #o/p = 10 so it is a integer division it will get adopt the decimal number
