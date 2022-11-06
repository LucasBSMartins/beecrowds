while True:
    n = int(input())
    if n == 0: break

    m = 0 
    
    for _ in range(n):
        _, a = map(int, input().split())
        m += a//2
    
    print(m//2)