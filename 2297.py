t = 1
while True:
    sa = 0
    sb = 0
    x = int(input())
    if x == 0:
        break
    print('Teste %d' %t)
    for i in range(0, x):
        a, b  = map(int, input().split())
        sa += a
        sb += b
    if sa > sb:
        print('Aldo')
        print('')
    elif sb > sa: 
        print('Beto')
        print('')
    t += 1