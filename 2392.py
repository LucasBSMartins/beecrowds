n , m = map(int, input().split())
l = [0]*n

for _ in range(m):
    p, d = map(int, input().split())    
    a = p-1
    while a >= 0:
        a -= d
    a += d
    for i in range(a, n, d):
        l[i] = 1
for v in l:
    print(v)