matrix1=[[1,2,3],
         [4,5,6],
         [7,8,9]]
matrix2=[[0,1,2,3],
         [4,5,6,7],
         [8,9,10,11]]
rmatrix=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            rmatrix[i][j]+=matrix1[i][k]*matrix2[k][j]
for r in rmatrix:
    print(r)
