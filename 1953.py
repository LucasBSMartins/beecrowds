while True:
    try:
        epr = ehd = intr = 0
        n = int(input())
        for i in range(n):
            l, curso= input().split()
            if curso == "EPR":
                epr += 1
            elif curso == "EHD":
                ehd += 1
            else:
                intr += 1
        
        print("EPR: %d" %epr)
        print("EHD: %d" %ehd)
        print("INTRUSOS: %d" %intr)
    except EOFError: break