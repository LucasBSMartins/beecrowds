n, m = map(int, input().split())
l= list(map(int, input().split()))
acc = 0
for i in range(0, n):
        if i == (n-1):
            d= 42195 - l[i]
            if d > m:
                print('N')
                acc += 1
                break
        else:
            d = l[i+1] - l[i]
            if d > m:
                print('N')
                acc +=1
                break

if acc == 0:
    print('S')