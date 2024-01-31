p1 = input().split()
p1s = str(p1[0])
p1t = int(p1[1])

p2 = input().split()
p2s = str(p2[0])
p2t = int(p2[1])

p3 = input().split()
p3s = str(p3[0])
p3t = int(p3[1])

if p1s == "Y" and p1t >= 37:
    if (p2s == "Y" and p2t >= 37) or (p3s == "Y" and p3t >= 37):
        print("E")
    else:
        print("N")

else:
    if (p2s == "Y" and p2t >= 37) or (p3s == "Y" and p3t >= 37):
        print("E")
    else:
        print("N")