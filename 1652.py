l, n = map(int, input().split())

a = [None] * 21
b = [None] * 21

for i in range(0,l):
    a[i], b[i] = input().split()
    
for _ in range(0, n):
    p = input()
    c = False
    
    for i in range(0, l):
        if a[i] == p:
            print(b[i])
            c = True
            break
            
    if not c:
        t = len(p)
        if t > 1 and p[t-1] == 'y' and not (p[t-2] == 'a' or p[t-2] == 'e' or p[t-2] == 'i' or p[t-2] == 'o' or p[t-2] == 'u') :
             print(p[0:t-1] + "ies")
        elif p[t-1] == 'o' or p[t-1] == 's' or p[t-1] == 'x':
            print(p + "es")
        elif t > 1 and p[t-1] == 'h' and (p[t-2] == 's' or p[t-2] == 'c'):
            print(p + "es")
        else:
            print(p + "s")