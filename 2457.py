n = input()
l= input().split()
total = 0 
for i in range(len(l)):
    if n in l[i]:
        total += 1
        
total /= len(l)/100

print('%.1f' %total)
