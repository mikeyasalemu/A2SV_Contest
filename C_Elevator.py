tests = int(input())
for i in range(tests):
    lst = list(map(int, input().split(" ")))
    ans = 0
    foot = 0
    elv = 0
    if lst[2] > 0:
        foot = lst[2] * lst[0]
        elv = lst[2] * lst[1] * 2
    if foot <= elv:
        ans += foot
    else:
        ans+= elv
    if lst[0] >= lst[1]:
        ans+= lst[1] * (4 - lst[2])
    else:
         ans+= lst[0] * (4 - lst[2])
    print(ans)