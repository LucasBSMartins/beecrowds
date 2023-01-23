n = int(input())
lingua = {}
for _ in range (n):
    
    idioma = input()
    transl = input()
    lingua[idioma] = transl
m = int(input())
for _ in range(m):
    nome = input()
    nat = input()
    print(nome)
    print(lingua[nat])
    print("")