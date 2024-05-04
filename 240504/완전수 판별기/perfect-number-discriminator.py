n = int(input())

num = 0

for i in range(1, n):
    if n % i == 0:
        num += i

if num == n:
    print("P")
else:
    print("N")