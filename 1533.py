while True:
    n = int(input())
    i = 0
    if n == 0:
        break
    else:
        l = list(map(int, input().split()))
        a = sorted(l, reverse=True)
        while True:
            if l[i] == a[1]:
                print(i+1)
                break
            i += 1