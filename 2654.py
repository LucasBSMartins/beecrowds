mp = 0
md = 0 
mm = 999999999999999
ordem = []
n = int(input())
for i in range(n):
    nome, p, d, m = input().split()
    p = int(p)
    d = int(d)
    m = int(m)
    ordem.append(nome)
    ordem = sorted(ordem)
    if p > mp :
        mp = p
        mn = nome 
        md = d
        mm = m
    elif p == mp:
        if d > md:
            mp = p
            mn = nome 
            md = d
            mm = m
        elif d == md:
            if m < mm:
                mp = p
                mn = nome 
                md = d
                mm = m
            elif m == mm:
                for j in range(n):
                    if ordem[j] == mn:
                        break
                    elif ordem[j] == nome:
                        mn = nome 
                        break
print(mn)       