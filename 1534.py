while True:
    try:
        n = int(input())
    except EOFError: break
    mat = [3] * n
    for i in range(n):
        mat[i] = [3] * n
    
    z = n-1
    
    for i in range(n):
        mat[i][i] = 1
        mat[i][z] = 2
        
        z-=1
    for i in range (0,len (mat)):
        for j in range (0,len(mat[i])):
            if j != 0:
                print("", end="")
            print("%d" %mat[i][j], end="")
            if (j == n-1):
                print ("")
    