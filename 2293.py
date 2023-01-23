n,m = map(int,input().split())

mat = [0]*n
for i in range(n):
    mat[i] = list(map(int, input().split()))
soma = [0] * (n*m*99)
for i in range(n):
    for j in range(m):
        soma[i] += mat[i][j]
        
for j in range(m):
    for i in range(n):
        soma[j+n] += mat[i][j]
    
print(max(soma))