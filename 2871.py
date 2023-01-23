while True:
    try:
        m,n = map(int,input().split())
    except EOFError: break
    
    soma = 0
    
    mat = [0] * m
    for i in range(m):
        mat[i] = list(map(int,input().split()))
    
    for i in range(m):
        for j in range(n):
            soma += mat[i][j]
      
    print("%d saca(s) e %d litro(s)" %((soma//60),(soma%60)))