n = int(input())
1 3 5 7 8 10 12
4 6 9 11
if n == 2:
    print(28)
else:
    if (n % 2 == 1 and n <= 7) or (n % 2 == 0 and n >= 8):
        print(31)
    else:
        print(30)