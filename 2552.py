while True:
    try:
        n,m = map(int, input().split())
        mat = [1] * n
        for i in range(n):
            mat[i] = list(map(int,input().split()))
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] = 9
        for i in range(n):
            for j in range(m):
                acc = 0
                if n == 1:
                    if j == 0:
                        if mat[i][j+1] == 9:
                            acc += 1
                            mat[i][j] = acc
                    if j == m-1:
                        if mat[i][j-1] == 9:
                            acc += 1
                            mat[i][j] = acc
                elif m == 1:
                    if i == 0:
                        if mat[i+1][j] == 9:
                            acc += 1
                            mat[i][j] = acc
                    if i == n-1:
                        if mat[i-1][j] == 9:
                            acc += 1
                            mat[i][j] = acc
                            
                elif mat[i][j] == 0:
                    if i == 0:
                        if j == 0:
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            mat[i][j] = acc
                        elif j == m-1:
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                        else:   
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                    elif i == n-1:
                        if j == 0:
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            mat[i][j] = acc
                        elif j == m-1:
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                        else:   
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                    else:
                         if j == 0:
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            mat[i][j] = acc
                         elif j == m-1:
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                         else: 
                            if mat[i+1][j] == 9:
                                acc += 1
                            if mat[i-1][j] == 9:
                                acc += 1
                            if mat[i][j+1] == 9:
                                acc += 1
                            if mat[i][j-1] == 9:
                                acc += 1
                            mat[i][j] = acc
                       
        
    
    
    
    
    
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print("", end="")
                print("%d" %mat[i][j], end="")
                if (j == m-1):
                    print ("")           
    
    
    
    except EOFError: break
