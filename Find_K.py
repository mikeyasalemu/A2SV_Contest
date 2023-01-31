size = int(input())
for i in range(size):
    size, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    valid = set(lst)
    check = False
    for i in range(size):
        if k + lst[i] in valid:
            check = True
    if check:
        print("YES")
    else:
        print("NO")
