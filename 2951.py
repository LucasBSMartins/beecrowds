n, g = map(int, input().split())
tec = {}

for _ in range(n):
    r, v = input().split()
    v = int(v)
    tec[r] = v
    
x = int(input())
l = list(input().split())
som = 0

for i in range(x):
    som += tec[l[i]]
    
print(som)
if som >= g:
    print("You shall pass!")
else:
    print("My precioooous")