ma, ea = input().split()
ma = int(ma)
ea = int(ea)
mb, eb = input().split()
mb = int(mb)
eb = int(eb)

if ma > mb:
    print("A")
elif mb > ma:
    print("B")
elif ea > eb:
    print("A")
else:
    print("B")