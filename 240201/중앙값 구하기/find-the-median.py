inp = input().split()
a, b, c = inp[0], inp[1], inp[2]

if a > b:
    if a < c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

else:
    if b < c:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)