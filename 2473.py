n = list(map(int, input().split()))
f = list(map(int, input().split()))
acc = 0

for i in range(len(n)):
    if f[i] in n:
        acc += 1
# vejo quantos numeros estão certos, e depois printo o resultado

if acc == 3:
    print("terno")
elif acc == 4:
    print("quadra")
elif acc == 5:
    print("quina")
elif acc == 6:
    print("sena")
else:
    print("azar")
