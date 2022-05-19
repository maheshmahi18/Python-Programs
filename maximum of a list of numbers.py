n=int(input("enter the number of elements in the list:"))
l=[]
for i in range(0,n):
     a=int(input())
     l.append(a)
max = l[0]
for i in range(0,n):
    if max<l[i]:
       max=l[i]
print("Maximum value is",max)
