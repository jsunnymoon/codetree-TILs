a, b = map(int, input().split())

print(a//b, end="")
print(".", end="")
for _ in range(20):
    print((a * 10) // b, end="")
    a == (a*10) % b