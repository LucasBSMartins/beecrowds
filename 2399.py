n = int(input())
l = []
for _ in range(0, n):
    l.append(int(input()))
    
for i in range(0, n):
    z = 0
    if n==1:
        if l[0]==1:
            z+=1
    else:
        if i==0:
            if l[1]==1:
                z += 1
            if l[0]==1:
                z += 1
        elif i==(n-1):
            if l[n-1]==1:
                z += 1
            if l[n-2]==1:
                z += 1
        else:
            if l[i-1]==1:
                z += 1
            if l[i]==1:
                z += 1
            if l[i+1]==1:
                z += 1
    print(z)