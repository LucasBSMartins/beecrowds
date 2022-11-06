print('MUITO OBRIGADO')

ca = 0
cg = 0
cd = 0

while True:
    x = int(input())
    if x == 1:
        ca = ca + 1
    elif x == 2:
        cg = cg + 1 
    elif x == 3:
        cd = cd + 1 
    elif x == 4:
        print('Alcool: %d' %ca)
        print('Gasolina: %d' %cg)
        print('Diesel: %d' %cd)
        break 
  