mat =[None] * 12
sum = 0
for l in range(0,12):
    mat[l] = [None] * 12
t = input()
for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())
f = 12    
for k in range(1,12):
    f -= 1
    for s in range(f,12):
        sum += mat[k][s] 

if t == "S":
    print("%.1f" %sum)
else: 
    print("%.1f" %(sum/66))