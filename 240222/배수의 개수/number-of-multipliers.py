three = 0
five = 0
for _ in range(10):
    inp = int(input())
    if inp % 3 == 0:
        three += 1
    if inp % 5 == 0:
        five += 1
    
print(three, five)