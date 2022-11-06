while True:
    try:
        m, d = map(int, input().split())
        if m == 12 and d == 24:
            print('E vespera de natal!')
        elif m == 12  and d == 25:
            print('E natal!')
        elif m == 12 and d > 24:
            print('Ja passou!')
        elif m == 12 and d < 24:
            print('Faltam %d dias para o natal!' %(25-d))
        elif m == 1:
            d = 31-d 
            print('Faltam %d dias para o natal!' %(329+d))
        elif m == 2:
            d = 29-d
            print('Faltam %d dias para o natal!' %(300+d))
        elif m == 3:
            d = 31-d
            print('Faltam %d dias para o natal!' %(269+d))
        elif m == 4:
            d = 30-d
            print('Faltam %d dias para o natal!' %(239+d))
        elif m == 5:
            d = 31-d
            print('Faltam %d dias para o natal!' %(208+d))   
        elif m == 6:
            d = 30-d
            print('Faltam %d dias para o natal!' %(178+d))
        elif m == 7:
            d = 31-d
            print('Faltam %d dias para o natal!' %(147+d))   
        elif m == 8:
            d = 31-d
            print('Faltam %d dias para o natal!' %(116+d))
        elif m == 9:
            d = 30-d
            print('Faltam %d dias para o natal!' %(86+d))   
        elif m == 10:
            d = 31-d
            print('Faltam %d dias para o natal!' %(55+d)) 
        elif m == 11:
            d = 30-d
            print('Faltam %d dias para o natal!' %(25+d))
    except EOFError:
        break