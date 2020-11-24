n,m = input().split()
a=[]
_sum = 0
for i in range (int(n)):
    list = [int(i) for i in input().split()]
    if(_sum < sum(list)):
        _sum = sum(list)
        vt_dau = i
    a.append(_sum)
print(str(_sum) + " " + str(a.index(_sum)))
    
