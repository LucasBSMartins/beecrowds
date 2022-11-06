o, b, i = map(float, input().split())

if o < b and o < i:
    print('Otavio')
if b < o and b < i:
    print('Bruno')
if i < b and i < o:
    print('Ian')
if o==b or o==i or i==b:
    print('Empate')