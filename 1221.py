import math
x = int(input())

for i in range(0,x):
    y = int(input())
    if y%2==0 and y != 2:
       print('Not Prime')
    elif y%3==0 and y!= 3:
       print('Not Prime')
    elif y%5==0 and y != 5:
       print('Not Prime')
    else:
        conta=0
        y1=int(math.sqrt(y))
        for a in range(2,y1+1):
            if y%a==0:
                conta+=1
                break
        if conta>0:
            print('Not Prime')
        else:
            print('Prime')