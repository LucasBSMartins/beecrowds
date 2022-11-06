mat =[None] * 12
sum = 0
for l in range(0,12):
    mat[l] = [None] * 12
t = input()
for i in range(0,12):
    for j in range(0,12):
        mat[i][j] = float(input())
f = 12   
z = 0
for k in range(0,5):
    f -= 1
    z +=1
    for s in range(z,f):
        sum += mat[k][s] 

if t == "S":
    print("%.1f" %sum)
else: 
    print("%.1f" %(sum/30))