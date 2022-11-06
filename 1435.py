while True:
    x = int(input())
    if x == 0: break
    mat = [1] * x
    for i in range(x):
        mat[i] = [1] * x
    for i in range(0,x):
        for j in range(0,x):
            if(i < x-i-1):
                dl = i
            else:
                dl = x-i-1
            
            if (j < x-j-1):
                dc = j
            else:
                dc = x-j-1
            
            d = min(dc,dl)
            mat[i][j] = d + 1
           
   
    for i in range (0,len (mat)):
        for j in range (0,len(mat[i])):
            if j != 0:
                print(" ", end="")
            print("%3d" %mat[i][j], end="")
            if (j == x-1):
                print ("")
    print()