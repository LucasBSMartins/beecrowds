while True:
    n = int(input())
    if n == 0: break

    p = 0
    l = list(map(int, input().split()))

    for i in range(1, n-1):
        if (l[i] > l[i-1] and l[i] > l[i+1]) or (l[i] < l[i-1] and l[i] < l[i+1]):
            p += 1

    if (l[0] > l[n-1] and l[0] > l[1]) or (l[0] < l[n-1] and l[0] < l[1]):
        p += 1
    if (l[n-1] > l[n-2] and l[n-1] > l[0]) or (l[n-1] < l[n-2] and l[n-1] < l[0]):
        p += 1

    print(p)