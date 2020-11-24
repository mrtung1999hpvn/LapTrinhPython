n = int(input())
a = []
kq = False
_sumcheo1 = 0
_sumcheo2 = 0
for i in range(n):
    list = [int(i) for i in input().split()]
    _sum = sum(list)
    if(_sum==sum(list)):
        kq = True
    else:
        kq = False
    _sumcheo1 = _sumcheo1 + list[i]
    _sumcheo2 = _sumcheo2 + list[n-i-1]
    a.append(list)

print(str(_sum) if kq == True and _sumcheo1 == _sumcheo2 and sum([sum(x) for x in zip(*a)])/n==_sumcheo1 else 'KHONG')
