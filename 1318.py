while True:
    n, _ = map(int, input().split())
    if n == 0: break

    l = list(map(int, input().split()))
    c = 0 
    l1 = []
    l2 = []
    for i in l:
        if i in l1:
            c += 1 
            if i in l2:
                c -= 1 
            l2.append(i)
        else:
            l1.append(i)
    print(c)