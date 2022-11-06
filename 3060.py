v = int(input())
p = int(input())

# Se a divisão for exata o valor das parcelas será sempre o mesmo

if v%p==0:
    for i in range(0,p):
        print('%d' %(v/p))
else:
    r = v%p
    for i in range(0, p):
        if r!=0:
            print('%d' %((v//p)+1))
            r -= 1
      	    # Basicamente um while	
	else:
            print('%d' %(v//p))
