n = int(input())
mat = [0] *n
for i in range(n):
    mat[i] = [0] * (n-i)

mat[0] = list(map(int, input().split()))
for i in range(1,n):
    for j in range((n-i)):
        if mat[i-1][j] == mat[i-1][j+1]:
            mat[i][j] = 1
        else:
            mat[i][j] = -1
        
if mat[n-1][0] == 1:
    print("preta")
else: 
    print("branca")
