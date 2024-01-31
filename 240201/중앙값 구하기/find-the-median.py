inp = input().split()
a, b, c = inp[0], inp[1], inp[2]

if a > b:
    if a < c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

elif a > c:
    if a < b:
        print(a)
    elif c > b:
        print(c)
    else:
        print(b)