x = int(input())
l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for _ in range(x):
    a = 0
    y = input()
    for c in y:
        a += l[int(c)]
    print(a, end=" ")
    print("leds")