n = int(input())
acc = 0
for i in range(0, n):
    a, b = (input().split())
    b = int(b)
    if a == 'G':
       acc -= b 
    else:
       acc += b
    # Se for um gasto da faculdade, ele diminui o valor, se for uma oferta de dinheiro do governo
    # soma, ao final se o valor der negativo continuará a greve
if acc < 0:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')
        
