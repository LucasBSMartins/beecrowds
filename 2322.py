n = int(input())
l = list(map(int, input().split()))

# vejo se dentro de 1 até n+1 tem a peça, se n tiver printo ela e paro o algoritmo

for i in range(1, n+1):
    if not i in l:
        print(i)
        break

