n = int(input())
sum = 0

for i in range(1, 100):
    if sum >= n:
        print(i-1)
        break
    sum += i