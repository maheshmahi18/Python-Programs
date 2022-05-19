n=int(input("Enter the no.of elements in the list:"))
l=[]
print("Enter the",n,"list elements in the ascending order")
for i in range(1,n+1):
    num=int(input())
    l.append(num)
print("The list elements are:",l)
print("Enter the element to be searched in the list")
x=int(input())
left=0
right=len(l)-1
count=0
while(left<=right):
    mid=(left+right)//2
    if x is l[mid]:
        count=count+1
        break
    elif x>l[mid]:
        left=mid+1
    else:
        right=mid-1
if count==0:
    print("Element is not found in the list")
else:
    print("Element is found",mid+1,"position in the list")
    
