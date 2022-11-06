i, n = map(int,input().split())
d=i
e=i
f=i

for _ in range(n):
    x = list(input().split())
    if x[0] == "C":
        x[2] = int(x[2])
        if x[1] == "D":
            d -= x[2]
        elif x[1] == "E":
            e -= x[2]
        elif x[1] == "F":
            f -= x[2]
    if x[0] == "V":
        x[2] = int(x[2])
        if x[1] == "D":
            d += x[2]
        elif x[1] == "E":
            e += x[2]
        elif x[1] == "F":
            f += x[2]
    if x[0] == "A":
        x[3] = int(x[3])
        if x[1]=="D":
            if x[2]=="E":
                e -= x[3]
                d += x[3]
            else:
                f -= x[3]
                d += x[3]
        if x[1]=="E":
            if x[2]=="D":
                d -= x[3]
                e += x[3]
            else:
                f -= x[3]
                e += x[3]
        if x[1]=="F":
            if x[2]=="E":
                e -= x[3]
                f += x[3]
            else:
                d -= x[3]
                f += x[3]
print("%d %d %d" %(d,e,f))