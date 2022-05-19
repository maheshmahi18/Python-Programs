n=int(input("enter a number:"))
a=0
while (n>0):
    r=n%10
    n=n//10
    a=a+r
print(a)
