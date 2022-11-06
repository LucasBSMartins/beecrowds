x = int(input())

for _ in range(x):
    l=[]
    s1, s2 = list(input().split())
    men = min(len(s1), len(s2))
    for i in range (men):
        l += s1[i] + s2[i]
        
    if len(s1) > len(s2):
        a = s1[men:]
    else:
        a = s2[men:]
    a = "".join(a)
    print("".join(l)+a)