l, c = map(int, input().split())
a, b = map(int, input().split())
a -= 1
b -= 1
mat = [0] * l

for i in range(l):
    mat[i] = list(map(int, input().split()))
z = True
if l == 1 and c == 1:
    print("1 1")
    z = False
    
while z:
    if l == 1 and c != 1:
        if b == 0:
            if mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
        elif b == (c-1):
            if mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
        else:
            if mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            elif mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False  
    elif l != 1 and c == 1:
        if a == 0:
            if b == 0:
                if mat[a+1][b] == 1:
                    mat[a][b] = 0
                    a += 1
                else:
                    print("%d %d" %(a+1,b+1))
                    z = False
        elif a == (l-1):
            if b == 0:
                if mat[a-1][b] == 1:
                    mat[a][b] = 0
                    a -= 1
                else:
                    print("%d %d" %(a+1,b+1))
                    z = False
        else:
            if mat[a-1][b] == 1:
                mat[a][b] = 0
                a -= 1
            elif mat[a+1][b] == 1:
                mat[a][b] = 0
                a += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
    elif a == 0:
        if b == 0:
            if mat[a+1][b] == 1:
                mat[a][b] = 0
                a += 1
            elif mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
        elif b == (c-1):
            if mat[a+1][b] == 1:
                mat[a][b] = 0
                a += 1                
            elif mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
        else:
            if mat[a+1][b] == 1:
                mat[a][b] = 0
                a += 1
            elif mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            elif mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
    elif a == (l-1):
        if b == 0:
            if mat[a-1][b] == 1:
                mat[a][b] = 0
                a -= 1
            elif mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1

            else:
                print("%d %d" %(a+1,b+1))
                z = False
        elif b == (c-1):
            if mat[a-1][b] == 1:
                mat[a][b] = 0
                a -= 1
            elif mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
        else:
            if mat[a-1][b] == 1:
                mat[a][b] = 0
                a -= 1
            elif mat[a][b-1] == 1:
                mat[a][b] = 0
                b -= 1
            elif mat[a][b+1] == 1:
                mat[a][b] = 0
                b += 1
            else:
                print("%d %d" %(a+1,b+1))
                z = False
    elif b == 0:
        if mat[a-1][b] == 1:
            mat[a][b] = 0
            a -= 1
        elif mat[a+1][b] == 1:
            mat[a][b] = 0
            a += 1
        elif mat[a][b+1] == 1:
            mat[a][b] = 0
            b += 1
        else:
            print("%d %d" %(a+1,b+1))
            z = False    
    elif b == (c-1):
        if mat[a-1][b] == 1:
            mat[a][b] = 0
            a -= 1
        elif mat[a+1][b] == 1:
            mat[a][b] = 0
            a += 1
        elif mat[a][b-1] == 1:
            mat[a][b] = 0
            b -= 1
        else:
            print("%d %d" %(a+1,b+1))
            z = False
    else:
        if mat[a-1][b] == 1:
            mat[a][b] = 0
            a -= 1
        elif mat[a+1][b] == 1:
            mat[a][b] = 0
            a += 1
        elif mat[a][b-1] == 1:
            mat[a][b] = 0
            b -= 1
        elif mat[a][b+1] == 1:
            mat[a][b] = 0
            b += 1
        else:
            print("%d %d" %(a+1,b+1))
            z = False



