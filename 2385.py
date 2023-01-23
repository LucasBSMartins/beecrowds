n = int(input())
p,q,r,s,x,y  = map(int, input().split())
a,b = map(int,input().split())
mata = [0] * n
matb = [0] * n
matc = 0

for j in range(n):
    mata[j] = (p * (a) + q * (j+1)) % x
    matb[j] = (r * (j+1) + s * (b)) % y
    
for i in range(n):
    matc += mata[i]*matb[i]
print(matc)