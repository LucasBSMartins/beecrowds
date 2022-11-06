while True:
    x = int(input())
    if x == 0: break
    mat = [0] * x
    for i in range(len(mat)):
        mat[i] = [0] * x 
    
    for i in range(x):
        for j in range(x):
            mat[i][j] = 2**(j+i)
    t = mat[x-1][x-1]
    t = len(str(t))
    t = int(t)
    if t == 1:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%1d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 2:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%2d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 3:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%3d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 4:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%4d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 5:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%5d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 6:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%6d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 7:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%7d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 8:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%8d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()
    if t == 9:
        for i in range (0,len (mat)):
            for j in range (0,len(mat[i])):
                if j != 0:
                    print(" ", end="")
                print("%9d" %mat[i][j], end="")
                if (j == x-1):
                    print ("")
        print()