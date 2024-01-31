inp = input().split()
a, b, c = inp[0], inp[1], inp[2]

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
elif a > c:
    if c > b:
        print(c)
    elif a > b:
        print(b)
    else:
        print(a)