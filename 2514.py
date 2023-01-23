def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
    
def mmc(a, b):
    return abs(a*b) / mdc(a, b)
    
while True:
    try:

        m = int(input())
        l1,l2,l3 = map(int,input().split())
        eclipse = mmc((mmc(l1,l2)),l3)
        x = eclipse - m
        x = int(x)
        print(x)
    except EOFError: break