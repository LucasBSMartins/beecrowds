while True:
    try:
        x = int(input())
    except EOFError: break
    if x == 0: break
    mat = [0] * x
    for i in range(len(mat)):
        mat[i] = [0] * x 
    z=0
    w=x-1
    y= x//3
    if x>7:
        for i in range(x):
            mat[i][z] = 2
            mat[i][w] = 3
            w-=1
            z+= 1
        for i in range(y,x-y):
            for j in range(y,x-y):
                mat[i][j]=1
            mat[x//2][x//2]=4
    elif x==7:
        for i in range(x):
            mat[i][z] = 2
            mat[i][w] = 3
            w-=1
            z+= 1
        for i in range(2,x-2):
            for j in range(2,x-2):
                mat[i][j]=1
        mat[x//2][x//2]=4
    elif x==5:
        for i in range(x):
            mat[i][z] = 2
            mat[i][w] = 3
            w-=1
            z+= 1
        for i in range(1,x-1):
            for j in range(1,x-1):
                mat[i][j]=1
        mat[x//2][x//2]=4
        
    
    
    for i in range (0,len (mat)):
        for j in range (0,len(mat[i])):
            if j != 0:
                print("", end="")
            print("%d" %mat[i][j], end="")
            if (j == x-1):
                print ("")
    print()
