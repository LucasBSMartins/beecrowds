som = 0
qt = 0
for i in range(0,6):
    x = float(input())
    if x > 0:
        som += x
        qt += 1
print("%d valores positivos" %qt )
print("%.1f" %(som/qt))