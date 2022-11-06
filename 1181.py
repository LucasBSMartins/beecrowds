mat =[None] * 12
sum = 0
for l in range(0,12):
    mat[l] = [None] * 12

x = int(input())
t = input()

for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())
for k in range(0,12):
    sum += mat[x][k]
if t == "S":
    print("%.1f" %sum)
else:
    print("%.1f" %(sum/12))
    