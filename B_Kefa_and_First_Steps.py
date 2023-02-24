n = int(input())
arr = list(map(int, input().split()))
left = 0
right = 1
ans = 1
while right < n:
    if arr[right] >= arr[right -1]:
        ans = max(ans, right - left +1)
        right+=1
    else:
        left = right
        right+=1
print (ans)
