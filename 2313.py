l = list(map(int,input().split()))


c=max(l)
l.remove(c)
a=l[0]
b=l[1]

if a+b>c:
    if a==b and b==c:
        print('Valido-Equilatero')
    elif a!=b and b!=c and c!=a:
        print('Valido-Escaleno')
    else:
        print('Valido-Isoceles')
    if a**2 + b**2 == c**2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')

else:
    print('Invalido')
    