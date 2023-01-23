n = int(input())
mat = [0]*n
for i in range(n):
    mat[i] = list(map(int,input().split()))
soma = [0]*(n*2)
v = 0
z = [0]*2
comp = [0]*2
nova = [[]]*2
s=0
x = 0

for i in range(n):
    for j in range(n):
        soma[i] += mat[i][j]
for i in range(n):
    for j in range(n):
        soma[i+n] += mat[j][i] 
for i in range((n*2)-1):
    if soma[i] == soma[i+1]:
        v += 1
    if v==2: 
        m = soma[i]
        break
for i in range((n*2)):
    if soma[i]!=m:
        if s == 2:
            z[s] = i-n
        else:
            z[s] = i
            s+=1
nova[0] = mat[z[0]]



erro = mat[z[0]][z[1]-n]
mat[z[0]][z[1]-n] = 0
for i in range(n):
    nova[1].append(mat[i][z[1]-n])
for i in range(2):
    for j in range(n):
        x += nova[i][j]
x -= 2*m
x /= -2

print("%d %.0f" %(x,erro) )
        

