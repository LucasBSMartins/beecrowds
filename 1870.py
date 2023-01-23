while True:
    l, c, p = map(int, input().split())
    if l == 0 and c == 0 and p == 0: break
    ve = 0
    vd = 0
    pe = 0
    pd = c-1
    v = False
    mat = [0]*l
    for i in range(l):
        mat[i] = list(map(int,input().split()))
    
    for i in range(l):
        for j in range((p-2),-1,-1):
            if mat[i][j]!=0:
                ve = mat[i][j]
                pe = j
                break
        for j in range(p,c):
            if mat[i][j]!=0:
                vd = mat[i][j]
                pd = j
                break
        
                
        dif = abs(vd - ve)
        
        if vd > ve:
            p -= dif
        elif ve > vd:
            p += dif
            
        if (p-1 <= pe):
            print("BOOM %d %d" %((i+1),(pe+1)))
            v = True
            break
        elif(p-1 >= pd):
            print("BOOM %d %d" %((i+1),(pd+1)))
            v = True
            break
    if not v:
        print("OUT %d" %p) 