ax1, ay1 = map(int, input().split())
ax2, ay2 = map(int, input().split())
ax3, ay3 = map(int, input().split())
ax4, ay4 = map(int, input().split())

bx1, by1 = map(int, input().split())
bx2, by2 = map(int, input().split())
bx3, by3 = map(int, input().split())
bx4, by4 = map(int, input().split())

#usando a regra do agrimensor pra achar a área

Aa = (abs(((ax1*ay2) + (ax2*ay3) + (ax3*ay4) + (ax4*ay1)) - ((ay1*ax2) + (ay2*ax3) + (ay3*ax4) + (ay4*ax1))))/2 
Ab = (abs(((bx1*by2) + (bx2*by3) + (bx3*by4) + (bx4*by1)) - ((by1*bx2) + (by2*bx3) + (by3*bx4) + (by4*bx1))))/2 

if Aa > Ab:
    print("terreno A")
else:
    print("terreno B")