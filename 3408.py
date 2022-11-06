n = int(input())
soma = 0
for i in range(n):
    p = list(input())
    for j in range(len(p)):
        if not(p[j]=="0" or p[j]=="1" or p[j]=="2" or p[j]=="3" or p[j]=="4" or p[j]=="5" or p[j]=="6"or p[j]=="7" or p[j]=="8" or p[j]=="9"):
            p[j] = ""
    p = "".join(p)
    p = int(p) 
    soma += p
print(soma)