n, k = map(int, input().split())
a = list(map(int, input().split()))
acc = 0

for i in range(n):
    if not (a[i] > 0):
        acc += 1
# verifico os q estão presentes, se o número for maior ou igual a k, printo sim, caso contrario não
if acc >= k:
    print("YES")
else: 
    print("NO")
