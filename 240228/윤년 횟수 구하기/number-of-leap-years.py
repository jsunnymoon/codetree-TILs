n = int(input())
leap_count = 0

for i in range(1, n+1):
    if i % 400 == 0:
        leap_count += 1
    elif i % 4 == 0 and i % 100 != 0:
        leap_count += 1



print(leap_count)