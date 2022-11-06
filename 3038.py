tec = {"@":"a", "&":"e", "!":"i", "*":"o", "#":"u"}

# crio um dicionario

while True:
    try:
        x = list(input())
        for i in range(len(x)):
            if x[i] in tec:
                x[i] = tec[x[i]]
        print("".join(x))
	#faço um for q verifica se o caractere está no dicionario, se ele estiver, eu faço a 		#troca   
    except EOFError: break
