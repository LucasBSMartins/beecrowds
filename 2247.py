t = 1
conta = 0
while True:
    n = int(input())
    if n != 0:
        print('Teste %d' %t )
        for i in range(1, n+1):
            j, z = map(int,
            input().split())
            conta = conta + (j-z)
            print(conta)
        print('')
    else:
        break
    conta = 0     
    t += 1 