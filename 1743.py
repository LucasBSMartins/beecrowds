l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
h = 0
for i in range(0, 5):
    if l[i] == l2[i]:
        h = 1
        break

if h==0:
    print('Y')
else:
    print('N')