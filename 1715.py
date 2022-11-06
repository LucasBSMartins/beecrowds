n,m = map(int, input().split())
soma = 0

for i in range(n):
    x = True
    l = list(map(int, input().split()))
    for j in range(m):
        if l[j] == 0:
            x = False
            break
    if x == True:
        soma += 1

print(soma)