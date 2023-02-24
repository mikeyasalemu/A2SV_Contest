size = int(input())
for i in range(size):
    length = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(length -1):
        if lst[i] + lst[i+1] < ((lst[i]*-1)+(lst[i +1]*-1)):
            lst[i]*=-1
            lst[i+1]*=-1
        
    print(sum(lst))
