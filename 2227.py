acc=1
while True:
    a, v = map(int, input().split())
    l = [0]*a
    if a==0 and v==0:
        break
    else:
        for i in range(v):
            x, y = map(int, input().split())
            l[x-1] += 1 
            l[y-1] += 1
        print('Teste %d' %acc)
        z = max(l)
        
        for j, n in enumerate(l):
            if n==z:
                print(j+1, end=' ')
        print()
        print()
        acc += 1