row = int(input("enter the row number:"))
col = int(input("enter the column number:"))

print("enter the elements for matrix1:")
matrix1 = [[int(input()) for i in range (col)] for j in range (row)]
print("The matrix1 is:")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end="")
    print()

print("enter the elements for matrix2:")
matrix2 = [[int(input()) for i in range (col)] for j in range (row)]
print("The matrix2 is:")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end="")
    print()

result = [[0 for i in range (col)] for j in range (row)]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("The result is:")
for i in range(row):
    for j in range(col):
        print(format(result[i][j],"<3"),end="")
    print()
