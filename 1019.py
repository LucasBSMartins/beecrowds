s = int(input())

h = s//3600
m = s//60 - h*60
s = s%60

print('%d:' % h + '%d:' % m + '%d' % s)