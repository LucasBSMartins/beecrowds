a, b, c = map(float,input().split())

d = (b**2 - 4 * a * c)

if d < 0 or 2*a==0:
    print('Impossivel calcular')
else: 
    r1 = (-b + (d)**0.5)/(2*a)
    r2 = (-b - (d)**0.5)/(2*a)
    print('R1 = %.5f' %r1)
    print('R2 = %.5f' %r2)