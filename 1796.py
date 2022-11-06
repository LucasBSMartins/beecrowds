a = int(input())
l = list(map(int, input().split()))
g, n = 0, 0

for i in range(0, a):
    if l[i]==0:
        g += 1
    else:
        n += 1
        
if g > n:
    print('Y')
else:
    print('N')