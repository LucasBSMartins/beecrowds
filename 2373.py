n = int(input())
soma = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    if a>b:
        soma += b
print(soma)