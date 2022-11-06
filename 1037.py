x = float(input())

if x>=0 and 25 >= x: 
    
    print('Intervalo [0,25]')

elif  x > 25 and 50 >= x: 
    
    print('Intervalo (25,50]')

elif x > 50 and 75 >= x:
    
    print('Intervalo (50,75]')
    
elif x > 75 and x <= 100 : 
    
    print('Intervalo (75,100]')
    
else:
    
    print('Fora de intervalo')