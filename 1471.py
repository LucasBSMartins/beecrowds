while True:
    try:
        n, r = map(int, input().split())
    except EOFError:
        break
    l = list(map(int, input().split()))
    
    if len(l) == n:
        print('*')
        continue
    
    for v in range(1, n+1):
        if not v in l:
            print(v, end=' ')
    print()
    