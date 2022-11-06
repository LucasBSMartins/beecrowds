x = int(input())

for i in range(x):
    x = int(input())
    if x%2==0:
        if x>0:
            print('EVEN POSITIVE')
        elif x<0: 
            print('EVEN NEGATIVE')
        else:
            print('NULL')
    elif x%2!=0:
        if x>0:
            print('ODD POSITIVE')
        elif x<0:
            print('ODD NEGATIVE')
        else:
            print('NULL')