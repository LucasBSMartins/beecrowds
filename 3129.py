n = int(input())
lista = []

for i in range(n):
    f = int(input())
    lista.append(f)

# crio uma lista sem repetidas com o comando "set"
lista2 = set(lista)
# printo a lista sem repetidas falando quantas figurinhas ele tem 
# pelo menos uma, depois faço a diferença das duas listas, que mostra
# a quantidade de repetidas
print(len(lista2))
print(len(lista)-len(lista2))