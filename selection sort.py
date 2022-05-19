a=[]
n=int(input("Enter the value of n:"))
for i in range(0,n):
    x=int(input())
    a.append(x)
print(a)
for i in range(0,n):
    s=min(a[i:])
    isa=a.index(s)
    a[i],a[isa]=a[isa],a[i]
print("Sorted order is:",a)

    
