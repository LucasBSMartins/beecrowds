n = int(input())

for _ in range(n):
    l = input()
    z = ""
    for i in range(len(l)-1,-1,-1):
        if l[i].islower():
            z += l[i]
    print(z)