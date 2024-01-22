h, w = input().split()
h = float(h) / 100
w = float(w)
BMI = int(w // h ** 2)
print(BMI)
if BMI >= 25:
    print("Obesity")