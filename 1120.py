while True:
    x, y = input().split()
    if x == "0" and y == "0": break
    y = list(y)
    for i in range(len(y)):
        if x in y:
            y.remove(x)
    if len(y) == 0:
        print("0")
    else:
        y = "".join(y)
        print(int(y))
        