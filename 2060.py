_ = int(input())

l = list(map(int,input().split()))
d2 = 0
d3 = 0
d4 = 0
d5 = 0
for i in range(len(l)):
    if l[i]%2 == 0:
        d2 += 1
    if l[i]%3 == 0:
        d3 += 1
    if l[i]%4 == 0:
        d4 += 1
    if l[i]%5 == 0:
        d5 += 1
print("%d Multiplo(s) de 2" %d2)
print("%d Multiplo(s) de 3" %d3)
print("%d Multiplo(s) de 4" %d4)
print("%d Multiplo(s) de 5" %d5)