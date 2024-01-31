inp = input().split()
a, b, c = inp[0], inp[1], inp[2]

if (b > a > c) or (c > a > b):
    print(a)
elif (a > b > c) or (c > b > a):
    print(b)
else:
    print(c)