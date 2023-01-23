n,m,s = map(int, input().split())
exercitoa = 0
exercitob = 0


for i in range(s):
    x,y,h = map(int,input().split())
    if n*y > m*x:
        exercitoa += h
    else:
        exercitob += h


print("%d %d" %(exercitoa, exercitob))