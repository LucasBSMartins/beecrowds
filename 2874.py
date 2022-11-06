while True:
    try:
        n = int(input())
        s = ""
        for _ in range(n):
            x = input().strip()
            m = 1
            a = 0
            for i in range(len(x)-1,-1,-1):
                if x[i] == "1":
                    a += m  
                m *= 2
            s += chr(a)
            
        print(s)
            
    
    
    except EOFError: break