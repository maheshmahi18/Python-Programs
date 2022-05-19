n=int(input("enter a number:"))
x=n
t=0
while (n>0):
    d=n%10
    t=t*10+d
    n=n//10
print(t)
