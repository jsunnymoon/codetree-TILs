sum = 0
cnt = 0

for i in range(10):
    num = int(input())
    if num >= 0 and num <= 200:
        sum += num
        cnt += 1

avg = sum/cnt
print(f"{sum} {avg:.1f}")