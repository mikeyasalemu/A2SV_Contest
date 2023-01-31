from collections import defaultdict
itr = int(input())
lst = list(map(int , input().split()))
minn = lst[0]
maxx = lst[0]
i = 1
count = 0
 
while i < itr:
    if lst[i] < minn and minn != lst[i]:
        minn = lst[i] 
        count+=1
    elif lst[i] > maxx and maxx != lst[i]:
        maxx = lst[i] 
        count+=1
    i+=1
print (count)
