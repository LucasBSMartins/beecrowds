import math 

c = int(input())

for _ in range(c):
   
    n = int(input())
    x, y = map(int, input().split())
    dm = 100000000000

    for i in range(n):
        n -= 1  
        x1, y1 = map(int, input().split())
        d = math.sqrt((abs(x1-x)**2) + (abs(y1-y)**2))
	# Pega a distância entre a bola branca e a outra         
        if d < dm:
           
            dm = d
            b = i + 1
	    # Se a distânica for menor que a menor ela recebe o valor da nova distância        
    print(b)
