n=int(input("enter the no.of elements in the list:"))
a=[]
sum=0
for i in range(0,n):
    x=int(input())
    a.append(x)
for i in a:
    sum=sum+i
print("Sum value is",sum)
