a, b = map(int, input().split())

mul5 = 0
mul7 = 0
cnt5 = 0
cnt7 = 0
while a <= b:
    if  a%5 == 0:
        mul5 += a
        cnt5 += 1
    if a%7 == 0:
        mul7 += a
        cnt7 += 1
    a += 1

sum = mul5 + mul7
cnt = cnt5 + cnt7
avg = sum/cnt
avg = round(avg, 1)
print(sum, avg)