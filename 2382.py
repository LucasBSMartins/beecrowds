l, a, p, r = map(int,input().split())

d = (l**2 + a**2 + p**2)**0.5

if d > (r*2):
    print('N')
else:
    print('S')