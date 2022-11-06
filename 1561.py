while True:
    try:
        h, m = map(int,input().split(":"))
        h = list(bin(h)[2:])
        m = list(bin(m)[2:])
        h = ["0"] * (4-len(h)) + h
        m = ["0"] * (6-len(m)) + m
    
        for i in range(len(h)):
            if h[i]=="0":
                h[i] =" "
            elif h[i] == "1":
                h[i] = "o"
        for j in range(len(m)):
            if m[j]=="0":
                m[j] =" "
            elif m[j] == "1":
                m[j] = "o"
        
        print(" ____________________________________________")
        print("|                                            |")
        print("|    ____________________________________    |_")
        print("|   |                                    |   |_)")
        print("|   |   8         4         2         1  |   |")
        print("|   |                                    |   |")
        print("|   |   %s         %s         %s         %s  |   |" %(h[0],h[1],h[2],h[3]))
        print("|   |                                    |   |")
        print("|   |                                    |   |")
        print("|   |   %s     %s     %s     %s     %s     %s  |   |"%(m[0],m[1],m[2],m[3],m[4],m[5]))
        print("|   |                                    |   |")
        print("|   |   32    16    8     4     2     1  |   |_")
        print("|   |____________________________________|   |_)")
        print("|                                            |")
        print("|____________________________________________|")
        print("")
    except EOFError: break