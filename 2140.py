notas = [100,50,20,10,5,2]
while True:
    valor,pago = map(int, input().split())
    if valor == pago == 0: break
    
    troco = pago - valor
    notausada = 0
    
    for nota in notas:
        
        if troco // nota > 0:
            x = troco//nota
            troco -= nota * x
            notausada += x
        if troco == 0:
            break
    
    if notausada == 2:
        print("possible")
    else:
        print("impossible")
