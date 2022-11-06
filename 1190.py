mat =[None] * 12
sum = 0
for l in range(0,12):
    mat[l] = [None] * 12
t = input()
for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())
f = 0
z = 11
for i in range(11,6,-1):
    f += 1
    z -= 1
    for j in range(z,f-1,-1):
        sum += mat[j][i] 

if t == "S":
    print("%.1f" %sum)
else: 
    print("%.1f" %(sum/30))