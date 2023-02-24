size = int(input())
for i in range(size):
    length = int(input())
    lst = list(map(int, input().split()))
    left = 0
    right = length -1
    check = True
    ans = []
    while left <= right:
        if check:
            ans.append(lst[left])
            left+=1
            check = False
        else:
            ans.append(lst[right])
            right -=1
            check = True

    print(*ans)

