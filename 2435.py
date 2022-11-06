n1, d1, v1 = map(int,input().split())
n2, d2, v2 = map(int,input().split())

v1 = v1/3.6
v2 = v2/3.6 

if (d2/v2) > (d1/v1):
    print(n1)
else:
    print(n2)