sp = 0
si = 0
spo = 0
sim = 0
for i in range(0,5):
    x = int(input())
    if x%2==0:
        sp +=1
    else:
        si += 1
    if x > 0:
        spo += 1
    if x < 0:
        sim += 1
print("%d valor(es) par(es)" %sp)
print("%d valor(es) impar(es)" %si)
print("%d valor(es) positivo(s)" %spo) 
print("%d valor(es) negativo(s)" %sim)