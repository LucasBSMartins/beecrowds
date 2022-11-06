while True:
    n,m = map(int,input().split())
    if n == 0 or m == 0: break
    mat = [1] * n
    for i in range(n):
        mat[i] = list(map(int,input().split()))
    r = 0
    z = 0
    z1 = 0
    z2 = 0
    z3 = 0
    for i in range(n):
        spoon = 0
        if 1 in mat[i]:
            z3 += 1 
        for j in range(m):
            if mat[i][j]==1:
                spoon += 1
        if spoon == m:
            z += 1
    if z == 0:
        r += 1
    if z3 ==n:
        r += 1
    
    for i in range(m):
        spoon1 = 0
        for j in range(n):
            if mat[j][i]==1:
                spoon1 += 1
            
        if spoon1 == 0:
            z2 += 1
        if spoon1 == n:
            z1 += 1    
    if z1 == 0:
        r += 1
    if z2 == 0:
        r += 1
    
    
    
    print(r)