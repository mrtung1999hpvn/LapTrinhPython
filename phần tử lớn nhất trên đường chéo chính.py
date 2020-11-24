n = int(input())
a = []
for i in range(n):
    lst=[int(i) for i in input().split()]
    a.append(lst)
    
max = a[0][0]
for i in range(n):
    if max < a[i][i]:
            max = a[i][i]
        
            
print(max)
