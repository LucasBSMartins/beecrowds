s = float(input())

if s <= 400.00:
    ns = s*(1.15)
    print('Novo salario: %.2f' %ns)
    print('Reajuste ganho: %.2f' %(s*(0.15)))
    print('Em percentual: 15 %')
elif s <= 800.00:
    ns = s*(1.12)
    print('Novo salario: %.2f' %ns)
    print('Reajuste ganho: %.2f' %(s*(0.12)))
    print('Em percentual: 12 %')
elif s <= 1200.00:
    ns = s*(1.10)
    print('Novo salario: %.2f' %ns)
    print('Reajuste ganho: %.2f' %(s*(0.10)))
    print('Em percentual: 10 %')
elif s <= 2000.00:
    ns = s*(1.07)
    print('Novo salario: %.2f' %ns)
    print('Reajuste ganho: %.2f' %(s*(0.07)))
    print('Em percentual: 7 %')
else:
    ns = s*(1.04)
    print('Novo salario: %.2f' %ns)
    print('Reajuste ganho: %.2f' %(s*(0.04)))
    print('Em percentual: 4 %')
