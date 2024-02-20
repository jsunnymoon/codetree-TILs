arr = input().split()
c = str(arr[0])
n = int(arr[1])

if c == "A":
    for i in range(n):
        print(i+1, end=" ")
else:
    for i in range(n):
        print(n-i, end=" ")