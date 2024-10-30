a= int(input("enter the first number"))
b=int(input("enter the second number"))
c=a+b
d=a-b
e=a*b
if b==0:
    print("division by zero is not possible")
else:
    f=a/b
j=input("choose your operator")
if j=='+':
    print("addition of the given number is %s"%c)
elif j=='-':
    print("subtraction of the given number is %s"%d)
elif j=='*':
    print("multiplication of the given number is %s"%e)
elif j=="/":
    print("division of the given number is %s"%f)
else:
    print("error")