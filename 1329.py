while True:
    n = int(input())
    if n == 0:
        break
    else:
        m, j = 0, 0
        l = list(map(int, input().split()))
        for i in range(0, len(l)):
            if l[i] == 0:
                m += 1
            elif l[i] == 1:
                j += 1
        print('Mary won %d' %m,'times and John won %d' %j,'times')
            
            