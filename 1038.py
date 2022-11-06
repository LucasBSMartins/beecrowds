x, y = map(int,input().split())

if x==1:
    print('Total: R$ %.2f' %(y*4.00))
elif x==2:
    print('Total: R$ %.2f' %(y*4.50))
elif x==3:
    print('Total: R$ %.2f' %(y*5.00))
elif x==4:
    print('Total: R$ %.2f' %(y*2.00))
else:
    print('Total: R$ %.2f' %(y*1.50))