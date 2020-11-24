n,m = input().split()
a=[]
duong =0
for i in range (int(n)):
    list = [int(i) for i in input().split()]
    if i==0 or i+1==int(n):
        for j in list:
            if j > 0:
                duong=duong+1
    else:
        if int(list[0]) >0:
            duong=duong+1
        if int(list[(len(list))-1])>0:
            duong=duong+1
    a.append(list)      
print(duong)
