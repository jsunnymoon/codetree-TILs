n = int(input())

sum = 0

for i in range(n):
    sum += int(input())

avg = sum/n

print(f"{sum} {avg:.1f}")