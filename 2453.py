l = list(input())

s = 0

for i in range(0,len(l),2):
   
    if s > (len(l)-1): break   
    if l[s] != " ":
        l[s]= ""
    else:
        l[s+1]= ""
        s += 1
    s += 2
        
print("".join(l))