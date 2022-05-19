r=int(input("no.of rows:"))
c=int(input("no.of column:"))
print("enter matrix elements:")
a=[[int(input()) for j in range (c)] for i in range (r)]
print(a)
print("Transpose of matrix is:")
for i in range(c):
    for j in range (r):
        print(a[j][i],end="\t")
    print("\n")

