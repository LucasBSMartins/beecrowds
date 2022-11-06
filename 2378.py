x, y = map(int, input().split())
c = 0
h = 0
for i in range(0, x):
    s, e = map(int, input().split()) 
    c += e - s
    if c > y:
        h += 1
if h >= 1:
    print('S')
else:
    print('N')