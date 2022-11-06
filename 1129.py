ver = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        for _ in range(0, n):
            l = list(map(int,input().split()))
            r = 0
            ver = 0
            for i in range(0, len(l)):
                if l[i] <= 127:
                    ver += 1
                    r = i
            if ver == 1:
                if r == 0: 
                    print('A')
                elif r == 1:
                    print('B')
                elif r == 2:
                    print('C')
                elif r == 3:
                    print('D')
                elif r == 4:
                    print('E')
            else:
                print('*')