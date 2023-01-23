n = int(input())
lista = []

for i in range(n):
    aluno = int(input())
    lista.append(aluno)

# uso o "set" que retira de uma lista todas as repetições
    
lista = set(lista)

print(len(lista))