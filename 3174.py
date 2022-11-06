n = int(input())
hb = 0
ha = 0
hm = 0
hd = 0
	
for i in range(n):
    e, g, h = input().split()
    h = int(h)
    if g == "bonecos":
        hb += h
    elif g == "arquitetos":
        ha += h
    elif g == "musicos":
        hm += h
    else:
        hd += h
# separo as horas trabalhadas por categoria e depois faço a soma da quantidade de brinquedos
acc = (hb//8) + (ha//4) + (hm//6) + (hd//12)
print(acc)
