size = int(input())
lst = list(map(int, input().split()))
lst.sort()
count_neg = 0
count  = 0
count_zero = 0
for i in range(size):
    if lst[i] < 0:
        count_neg +=1
        count += abs(lst[i] + 1)
    elif lst[i] > 0:
        count += lst[i] -1
    elif lst[i] == 0:
        count_zero +=1
        if count_zero > 0:
            count+=1
        elif count_zero == 1:
            index = i
if count_zero == 0 and count_neg % 2 != 0:
    count+=2
print (count)



