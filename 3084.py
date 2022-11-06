while True:
    try:
        x, y= map(int, input().split())
        print('%02d:%02d' %((x/30), (y/6)))
    except EOFError:
        break    