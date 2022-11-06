n, b, h, w = map(int, input().split())
c = [9999999999999999] * h
#boto um valor ridiculamente alto, pra poder comparar depois

for i in range(h):
    v = 0
    p = int(input())
    a = list(map(int,input().split()))
    
    for z in range(len(a)):
        if a[z] >= n:
            v = 1
    #verifico se vai ter quarto disponivel, se tiver prossigo e adiciono o valor na list de valores	
    if v == 1:
        c[i] = (n*p) 
    # comparo se o menor valor é menor q o orçamento se nao for, printo "stay home" 
if min(c) <= b:
    print(min(c))
else:
    print("stay home")
