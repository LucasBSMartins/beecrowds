p, n = map(int, input().split())
l = list(map(int, input().split()))
h = 0
for i in range (0, n-1):
    d = 0
    if l[i] >= l[i+1]:
        d = l[i] - l[i+1]
        if d > p:
            h = 1
            break
    else:
        d = l[i+1] - l[i]
        if d > p:
            h = 1
            break
if h == 0:
    print('YOU WIN')
else:
    print('GAME OVER')
        
                 