com = 1
while True:
    x= int(input())
    if x == (-1): break
    
    p = ((2**x)+1)**2
    
    print("Teste %d"%com)
    print(p)
    print("")
    com += 1