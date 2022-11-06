a = int(input())

b = a//365
c = a%365 // 30
d = (a%365)%30

print('%d ano(s)' %b)
print('%d mes(es)' %c)
print('%d dia(s)' %d)