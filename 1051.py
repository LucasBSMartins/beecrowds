n = float(input())

if n <= 2000.00:
    print("Isento")
if n > 2000.00 and n <= 3000.00:
    t = (n - 2000.00)*0.08
    print("R$ %.2f" %t)
if n > 3000.00 and n <= 4500.00:
    t = (1000.00*0.08) + (n-3000.00)*0.18
    print("R$ %.2f" %t)
if n > 4500.00:
    t = (1000.00*0.08) + (1500.00*0.18) + (n-4500.00)*0.28
    print("R$ %.2f" %t)