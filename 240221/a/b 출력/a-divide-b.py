a, b = map(int, input().split())

print(a//b, end="")
print(".", end="")
a %= b
for _ in range(20):
    a *= 10
    print(a // b, end="")
    a %= b