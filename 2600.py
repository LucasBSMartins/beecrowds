n = int(input())

for _ in range(n):
    som = 0
    l = [0] * 6  
    l2 = int(input())
    l0,l1,l5,l4 = map(int,input().split())
    l3 = int(input())
    l[0] = l0
    l[1] = l1
    l[2] = l2
    l[3] = l3
    l[4] = l4
    l[5] = l5
    for i in range(1,7):
        if not i in l:
            som += 1
    if l[0]+l[5]==7 and l[2]+l[3]==7 and l[1]+l[4]==7 and som==0:
        print("SIM")
    else:
        print("NAO")