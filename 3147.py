h, e, a, o, w, x = map(int, input().split())

a1 = h + e + a + x
a2 = o + w

# Se o exercito a1 for maior printa x, se for o a2 printa y
if a2 > a1:
    print('Sauron has returned.')
else:
    print('Middle-earth is safe.')
