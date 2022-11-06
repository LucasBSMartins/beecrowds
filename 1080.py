ma = 0


for i in range(1, 101):
    n = int(input())
    
    if ma < n:
        ma = n
        me = i
print(ma)
print(me)
    