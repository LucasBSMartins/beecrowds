x = int(input())

a = x//100
b = (x%100)//50
c = ((x%100)%50)//20
d = (((x%100)%50)%20)//10
e = ((((x%100)%50)%20)%10)//5
f = (((((x%100)%50)%20)%10)%5)//2
g = (((((x%100)%50)%20)%10)%5)%2










print(x)
print('%d nota(s) de R$ 100,00' %a)
print('%d nota(s) de R$ 50,00' %b)
print('%d nota(s) de R$ 20,00' %c)
print('%d nota(s) de R$ 10,00' %d)
print('%d nota(s) de R$ 5,00' %e)
print('%d nota(s) de R$ 2,00' %f)
print('%d nota(s) de R$ 1,00' %g)
