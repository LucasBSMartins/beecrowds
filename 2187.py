teste = 1
while True:
    n = int(input())
    if n != 0: 
        print('Teste %d' %teste)
        a = n//50   
        b = (n%50)//10
        c = ((n%50)%10)//5
        d = ((n%50)%10)%5
        print(a, b, c, d)
        print('')
    else:
        break
    teste += 1