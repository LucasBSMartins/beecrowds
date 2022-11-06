x, y = map(int,input().split())
c = y
m = y
for i in range(0, x):
    z = int(input())
    c += z 
    if c < m:
        m = c
   
print(m)
    