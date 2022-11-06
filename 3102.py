import math
x = int(input())
for i in range(0,x):
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    A = (xa*yb *1)+(ya*1*xc)+(1*xb*yc)-((ya*xb*1)+(xa*1*yc)+(1*yb*xc)) 
    print('%.3f' %(abs(A)/2))