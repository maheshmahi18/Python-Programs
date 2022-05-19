n=int(input("enter no.of terms:"))
a=-1
b=1
i=1
while(i<=n):
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1
