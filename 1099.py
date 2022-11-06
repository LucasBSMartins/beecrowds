n = int(input())

for _ in range (n):
    d = 0
    x, y = map(int,input().split())
    if x <= y:
        a=x
        b=y
    else:
        a=y
        b=x
    for i in range (a+1, b):
        if i%2==1:
            d = d + i
    print(d)