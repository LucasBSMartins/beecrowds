a = 0
e = 0
h = 0
m = 0
x = 0
n = int(input())
for s in range(n):
    _, z = input().split()
    if z == "A":
        a += 1
    elif z == "E":
        e += 1 
    elif z == "H":
        h += 1 
    elif z == "M":
        m += 1 
    elif z == "X":
        x += 1 
    

print("%d Hobbit(s)" %x)
print("%d Humano(s)" %h)
print("%d Elfo(s)" %e)
print("%d Anao(oes)" %a)
print("%d Mago(s)" %m)
