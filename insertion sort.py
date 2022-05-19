a=[]
n=int(input("enter the value of n:"))
for i in range(0,n):
    x=int(input())
    a.append(x)
print(a)
for i in a:
    j=a.index(i)
while j>0:
    if(a[j-1]>a[j]):
        a[j-1],a[j]=a[j],a[j-1]
    else:
        break
    j=j-1
print("sorted order is:",a)
