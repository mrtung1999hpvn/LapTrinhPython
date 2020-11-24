n = int(input())

list = [int(i) for i in input().split()]
chan = []
le = []
for j in list:
    if j%2==0:
        chan.append(j)
    else:
        le.append(j)
new = sorted(le,reverse=True) + sorted(chan)
kq=''
for j in new:
    kq += str(j)+" "

print(kq[:-1])
