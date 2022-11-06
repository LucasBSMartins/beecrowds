_, k = map(int, input().split())
l = list(map(int, input().split()))

p = 0
for i in range(1, len(l)-1):
    if l[i] > l[i+1] and l[i] > l[i-1]:
        p += 1

if p == k:
    print('beautiful')
else:
    print('ugly')
    