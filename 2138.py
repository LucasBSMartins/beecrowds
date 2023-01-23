while True:
    try:
        x = list(input())
        x= list(map(int, x))
        
        soma = [0] * 10
        for i in range(10):
            soma[i] += x.count(i)
            
        z = max(soma)
        for i in range(9,-1,-1):
            if soma[i] == z:
                print(i)
                break
    except EOFError: break