n, m = map(int,input().split())
e = True
a = False
esquerda = 0
nume = 0
mat = [0]*n


for i in range(n):
    mat[i] = list(map(int, input().split()))


    if a:
        if mat[i] != [0]*m:
            e = False
            break
            # se a linha inteira embaixo de um cheia de zeros 
            # nao estiver cheia de zeros, não é uma escada
    else:
        if mat[i] == [0]*m:
            a = True
            # se isso for verdade a linha inteira está cheia de zeros
        else:
            for j in range(m):
                if mat[i][j] > 0:
                    nume = j
                    break
                    # marco a posição do elemento a mais a esquerda diferente de zero      
            if (esquerda >= nume) and (i > 0):
                e = False
                break
                # se o numero mais a esquerda da linha anterior  for maior que o numero mais a esquerda diferente de zero desta linha
                # quer dizer que não é uma escada
            esquerda = nume
            # boto o numero mais a esquerda diferente de 0 desta linha pra testar na proxima linha
            


if e:
    print("S")
else:
    print("N")
                