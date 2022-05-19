arr=[]
n=int(input("Enter a no.of elements in the list:"))
for i in range(1,n):
    print("Enter",i,"number:")
    num=int(input())
    arr.append(num)
print(arr)
x=int(input("Enter the number to be searched:"))
count=0
for i in range(len(arr)):
    if arr[i]==x:
        count=count+1
        print("Element is found in",i+1,"position")
        break;
    if (count==0):
        print("Element not found in List")
    
