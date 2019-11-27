n = int(input("nhap n: "))
m = int(input("nhap m: "))
s = 0
for i in range(n,m+1):
    if i % 7 == 0 and i % 5 != 0:
        s = s + i
        print(s)