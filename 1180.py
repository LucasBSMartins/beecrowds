n = int(input())
l = list(map(int, input().split()))

for i in range(0, len(l)):
    if i == 0:
        men = l[0]
        pos = i 
    if l[i] < men:
        men = l[i]
        pos = i
print('Menor valor: %d' %(men))
print('Posicao: %d' %(pos))