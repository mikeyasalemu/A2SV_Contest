cases = int(input())
for i in range(cases):
    size, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 1
    res = 0
    for i in range(size - 1):
        if arr[i] < arr[i + 1] * 2:
            count +=1
        else:
            count = 1
        if count > k:
            res +=1
    print (res)
