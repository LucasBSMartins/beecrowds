while True:
    p, n, c = map(int, input().split())
    if p == 0: break

    l = [0]*p
    np = 0
    
    for _ in range(n):
        a = list(map(int, input().split()))
        for i in range(p):
            if a[i] == 1:
                l[i] += 1
            else:
                if l[i] >= c:
                    np += 1
                l[i] = 0
    
    for a in l:
        if a >= c:
            np += 1
    print(np)