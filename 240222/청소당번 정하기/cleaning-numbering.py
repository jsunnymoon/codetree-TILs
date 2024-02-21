n = int(input())

cr = 0
cor = 0
br = 0

for i in range(1, n+1):
    if i % 2 == 0:
        if i % 12 == 0:
            br += 1
        elif i % 3 == 0:
            cor += 1
        else:
            cr += 1
    elif i % 3 == 0:
        if i % 12 == 0:
            br += 1
        else:
            cor += 1

print(cr, cor, br)