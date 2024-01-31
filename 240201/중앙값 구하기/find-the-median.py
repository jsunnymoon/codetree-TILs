inp = input().split()
a, b, c = inp[0], inp[1], inp[2]

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)

else:
    if a < b and a > c:
        print(a)
    elif a < b and b < c:
        print(b)
    else:
        print(c)