d = [None] * 61
e = [None] * 61

while True:
    try:
        n = int(input())
    
        for i in range(30, 61):
            d[i] = 0
            e[i] = 0
        
        for i in range(n):
            m,l = input().split()   
            if l == 'D':
                d[int(m)] += 1
            else:
                e[int(m)] += 1
        acc = 0
        for i in range(30, 61):
            if d[i] < e[i]:
                acc += d[i]
            else:
                acc += e[i]
        
        
        print(acc)
        
    except EOFError:
        break