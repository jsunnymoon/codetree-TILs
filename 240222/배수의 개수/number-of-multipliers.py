three = 0
five = 0
for _ in range(10):
    inp = int(input())
    if inp % 3 == 0 and inp % 5 == 0:
        three += 1
        five += 1
    elif inp % 3 == 0:
        three += 1
    elif inp % 5 == 0:
        five += 1
    
print(f"{three} {five}")