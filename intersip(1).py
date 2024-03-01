'''
a=int(input("Enter a no"))
b=int(input("Enter a no"))
add=int(a) + int(b)
print(add)
'''
'''
a=int(input("Enter a no"))
b=int(input("Enter a no"))
if a>b:
    print("a is greater")
    if b>a:
        print("b is greater")

'''
'''
a=int(input("Enter a no"))
fact=1
if a<0:
    print("Not a factorial no")
elif a==0:
    print(1)
else:
    for i in range(1,a+1):
        fact=fact*i
        print(fact)
'''
'''
p=int(input("enter p"))
r=int(input("enter r"))
t=int(input("enter t"))
s=(p*r*t)/100
print(s)
'''
'''
p=int(input("enter p"))
r=int(input("enter r"))
n=int(input("no of interest"))
t=int(input("no of time period"))
C=p(1+(r/n))^nt
print(C)
'''
'''
a=int(input("enter a no"))
sum=0
b=a
while b>0:
    c=b%10
    sum+= c**3
    b //=10
    if a ==sum:
        print("Arm no")
    else:
        print("no arm")
        '''
'''
import math
r=int(input("enter radius:"))
A=math.pi*r*r
print(A)
'''
'''
a=int(input("enter a no"))
b=False
if a==1:
    print("not prime")
elif a>1:
    for i in range(2,a):
        if(a%i)==0:
            b=True
            break
        if b:
            print("is not prime")
        else:
            print("is prime")
            '''

'''
def fibonacci(n):
    if n<=0:
        print("incorrect")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        fibonacci(n-1)+fibonacci(n-2)
    print(fibonacci(10))
    '''