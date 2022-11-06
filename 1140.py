while True:
    x = input().split()
    s = True
    if x[0][0] == "*": break
    for i in range(len(x)):
        x[i] = x[i].lower()
    c = x[0][0]
    for i in range(1, len(x)):
        if x[i][0] != c:
            s = False
            break
    if s:
        print("Y")
    else:
        print("N")