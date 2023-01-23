while True:
    try:
        m,n = map(int,input().split())
        mat = [0] * m
        for i in range(m):
            mat[i] = list(input().split())
        pos = [0]*2
        for i in range(m):
            a = True
            for j in range(n):
                if mat[i][j] == "X":
                    pos[0] = i
                    pos[1] = j
                    a = False
                    break
            if not a: break
        a = True        
        if pos[0] == 0:
            if pos[1] == 0:
                if mat[pos[0]+1][pos[1]] == "0": aux = 2
                elif mat[pos[0]][pos[1]+1] == "0": aux = 4
            elif pos[1] == (n-1):
                if mat[pos[0]+1][pos[1]] == "0": aux = 2
                elif mat[pos[0]][pos[1]-1] == "0": aux = 3
            else:
                if mat[pos[0]+1][pos[1]] == "0": aux = 2
                elif mat[pos[0]][pos[1]-1] == "0": aux = 3
                elif mat[pos[0]][pos[1]+1] == "0": aux = 4
        elif pos[0] == (m-1):
            if pos[1] == 0:
                if mat[pos[0]-1][pos[1]] == "0": aux = 1
                elif mat[pos[0]][pos[1]+1] == "0": aux = 4
            if pos[1] == (n-1):
                if mat[pos[0]-1][pos[1]] == "0": aux = 1
                elif mat[pos[0]][pos[1]-1] == "0": aux = 3
            else:
                if mat[pos[0]-1][pos[1]] == "0": aux = 1
                elif mat[pos[0]][pos[1]-1] == "0": aux = 3
                elif mat[pos[0]][pos[1]+1] == "0": aux = 4
        elif pos[1] == 0:
            if mat[pos[0]-1][pos[1]] == "0": aux = 1
            elif mat[pos[0]+1][pos[1]] == "0": aux = 2
            elif mat[pos[0]][pos[1]+1] == "0": aux = 4
        elif pos[1] == (n-1):
            if mat[pos[0]-1][pos[1]] == "0": aux = 1
            elif mat[pos[0]+1][pos[1]] == "0": aux = 2
            elif mat[pos[0]][pos[1]-1] == "0": aux = 3
        else:  
            if mat[pos[0]-1][pos[1]] == "0": aux = 1
            elif mat[pos[0]+1][pos[1]] == "0": aux = 2
            elif mat[pos[0]][pos[1]-1] == "0": aux = 3
            elif mat[pos[0]][pos[1]+1] == "0": aux = 4
                
        #1 cima
        #2 baixo
        #3 esquerda
        #4 direita
        
        while a:
            if pos[0] == 0:
                if pos[1] == 0:
                    if mat[pos[0]+1][pos[1]] == "0":
                        if aux == 2:
                            print("F", end=" ")
                        elif aux == 4:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 2
                        elif aux == 3:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 2
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] += 1
                    elif mat[pos[0]][pos[1]+1] == "0":
                        if aux == 4:
                            print("F", end=" ")
                        elif aux == 1:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 4
                        elif aux == 2:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 4
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] += 1
                    else:
                        print("E")
                        a = False
                elif pos[1] == (n-1):
                    if mat[pos[0]+1][pos[1]] == "0":
                        if aux == 2:
                            print("F", end=" ")
                        elif aux == 4:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 2
                        elif aux == 3:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 2
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] += 1
                    elif mat[pos[0]][pos[1]-1] == "0":
                        if aux == 3:
                            print("F", end=" ")
                        elif aux == 1:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 3
                        elif aux == 2:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 3
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] -= 1        
                    else:
                        print("E")
                        a = False
                else:
                    if mat[pos[0]+1][pos[1]] == "0":
                        if aux == 2:
                            print("F", end=" ")
                        elif aux == 4:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 2
                        elif aux == 3:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 2
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] += 1
                    elif mat[pos[0]][pos[1]-1] == "0":
                        if aux == 3:
                            print("F", end=" ")
                        elif aux == 1:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 3
                        elif aux == 2:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 3
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] -= 1
                    elif mat[pos[0]][pos[1]+1] == "0":
                        if aux == 4:
                            print("F", end=" ")
                        elif aux == 1:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 4
                        elif aux == 2:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 4
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] += 1
                    else:
                        print("E")
                        a = False
        
            elif pos[0] == (m-1):
                if pos[1] == 0:
                    if mat[pos[0]-1][pos[1]] == "0":
                        if aux == 1:
                            print("F", end=" ")
                        elif aux == 3:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 1
                        elif aux == 4:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 1
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] -= 1
                    elif mat[pos[0]][pos[1]+1] == "0":
                        if aux == 4:
                            print("F", end=" ")
                        elif aux == 1:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 4
                        elif aux == 2:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 4
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] += 1
                    else:
                        print("E")
                        a = False
                if pos[1] == (n-1):
                    if mat[pos[0]-1][pos[1]] == "0":
                        if aux == 1:
                            print("F", end=" ")
                        elif aux == 3:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 1
                        elif aux == 4:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 1
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] -= 1
            
                    elif mat[pos[0]][pos[1]-1] == "0":
                        if aux == 3:
                            print("F", end=" ")
                        elif aux == 1:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 3
                        elif aux == 2:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 3
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] -= 1
                    else:
                        print("E")
                        a = False
                else:
                    if mat[pos[0]-1][pos[1]] == "0":
                        if aux == 1:
                            print("F", end=" ")
                        elif aux == 3:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 1
                        elif aux == 4:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 1
                        mat[pos[0]][pos[1]] = "1"
                        pos[0] -= 1
                    elif mat[pos[0]][pos[1]-1] == "0":
                        if aux == 3:
                            print("F", end=" ")
                        elif aux == 1:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 3
                        elif aux == 2:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 3
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] -= 1
                    elif mat[pos[0]][pos[1]+1] == "0":
                        if aux == 4:
                            print("F", end=" ")
                        elif aux == 1:
                            print("R",end=" ")
                            print("F",end=" ")
                            aux = 4
                        elif aux == 2:
                            print("L",end=" ")
                            print("F",end=" ")
                            aux = 4
                        mat[pos[0]][pos[1]] = "1"
                        pos[1] += 1
                    else:
                        print("E")
                        a = False
                    
            elif pos[1] == 0:
                if mat[pos[0]-1][pos[1]] == "0":
                    if aux == 1:
                        print("F", end=" ")
                    elif aux == 3:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 1
                    elif aux == 4:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 1
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] -= 1
                elif mat[pos[0]+1][pos[1]] == "0":
                    if aux == 2:
                        print("F", end=" ")
                    elif aux == 4:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 2
                    elif aux == 3:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 2
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] += 1
                elif mat[pos[0]][pos[1]+1] == "0":
                    if aux == 4:
                        print("F", end=" ")
                    elif aux == 1:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 4
                    elif aux == 2:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 4
                    mat[pos[0]][pos[1]] = "1"
                    pos[1] += 1
                else:
                    print("E")
                    a = False
        
            elif pos[1] == (n-1):
                if mat[pos[0]-1][pos[1]] == "0":
                    if aux == 1:
                        print("F", end=" ")
                    elif aux == 3:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 1
                    elif aux == 4:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 1
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] -= 1
                elif mat[pos[0]+1][pos[1]] == "0":
                    if aux == 2:
                        print("F", end=" ")
                    elif aux == 4:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 2
                    elif aux == 3:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 2
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] += 1
                elif mat[pos[0]][pos[1]-1] == "0":
                    if aux == 3:
                        print("F", end=" ")
                    elif aux == 1:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 3
                    elif aux == 2:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 3
                    mat[pos[0]][pos[1]] = "1"
                    pos[1] -= 1
                else:
                    print("E")
                    a = False
        
            
            else:  
                if mat[pos[0]-1][pos[1]] == "0":
                    if aux == 1:
                        print("F", end=" ")
                    elif aux == 3:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 1
                    elif aux == 4:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 1
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] -= 1
                elif mat[pos[0]+1][pos[1]] == "0":
                    if aux == 2:
                        print("F", end=" ")
                    elif aux == 4:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 2
                    elif aux == 3:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 2
                    mat[pos[0]][pos[1]] = "1"
                    pos[0] += 1
                elif mat[pos[0]][pos[1]-1] == "0":
                    if aux == 3:
                        print("F", end=" ")
                    elif aux == 1:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 3
                    elif aux == 2:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 3
                    mat[pos[0]][pos[1]] = "1"
                    pos[1] -= 1
                elif mat[pos[0]][pos[1]+1] == "0":
                    if aux == 4:
                        print("F", end=" ")
                    elif aux == 1:
                        print("R",end=" ")
                        print("F",end=" ")
                        aux = 4
                    elif aux == 2:
                        print("L",end=" ")
                        print("F",end=" ")
                        aux = 4
                    mat[pos[0]][pos[1]] = "1"
                    pos[1] += 1
                else:
                    print("E")
                    a = False
        
    except EOFError: break
        
        
        
        
