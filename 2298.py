n = int(input())
s = 1
for _ in range(n):
    x = list(map(int,input().split()))
    x.sort()
    pont = 0 
    if x[1] == (x[0]+1) and x[2] == (x[0]+2) and x[3] == (x[0]+3) and x[4] == (x[0]+4):
        pont += 200 + x[0]
    elif (x[0] == x[1] and x[0] == x[2] and x[0] == x[3]) or (x[1] == x[2] and x[1] == x[3] and x[1] == x[4]):
        pont += 180 + x[2]
    elif (x[0] == x[1] and x[2] == x[3] and x[2] == x[4]) or (x[4] == x[3] and x[2] == x[1] and x[2] == x[0]):
        pont += 160 + x[2]
    elif (x[0] == x[1] and x[0] == x[2]) or (x[1] == x[2] and x[1] == x[3]) or (x[2] == x[3] and x[2] == x[4]):
        pont += 140 + x[2]
    elif (x[0] == x[1] and x[2] == x[3]) or (x[1] == x[2] and x[3] == x[4]) or (x[0] == x[1] and x[3] == x[4]):
        pont += (3*x[3]) + (2*x[1]) + 20
    elif (x[0] == x[1]):
        pont += x[0]
    elif (x[1] == x[2]):
        pont += x[1]
    elif (x[2] == x[3]):
        pont += x[2]
    elif (x[3] == x[4]):
        pont += x[4]
    print("Teste %d" %s)
    print(pont)
    print("")
    s += 1