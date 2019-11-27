L = []
n = int(input("nhap so phan tu list: "))
for i in range(0,n):
    m = float(input("nhap phan tu list: "))
    L.append(m)
trungbinh = sum(L)/len(L)
for j in range(1,n):
    if j > trungbinh:
        print(L[j])