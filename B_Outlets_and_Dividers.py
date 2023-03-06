tests = int(input())
for i in range(tests):
    std , divider = map(int, input().split())
    lst = list(map(int, input().split(" ")))
    lst.sort(reverse=True)
    if std <= 2:
        print (0)
    else:
        ans = 1
        check = False
        for i in range(len(lst)):
            if ans + lst[i] >= std:
                ans += lst[i]
                check = True
                print(i +1)
                break
            else:
                ans+= lst[i] -1
        if not check:
            print(-1)