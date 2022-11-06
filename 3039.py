n = int(input())
c = 0
b = 0

for i in range(n):
    name, sex = input().split()
    if sex == "F":
        b += 1
    else:
        c += 1
# se for M somo um carrinho, se for F uma boneca, no final printo o total 
print("%d carrinhos" %c)
print("%d bonecas" %b)
