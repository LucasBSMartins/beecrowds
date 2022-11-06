l = list(map(float,input().split()))
area = ((l[0]+l[1])*l[2])/2

m = max(l)
l.remove(m)
a = l[0]
b = l[1]

if a+b > m:

    print('Perimetro = %.1f' %(a+b+m))
    
else:
    
    print('Area = %.1f' %area)