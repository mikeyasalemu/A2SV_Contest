n = int(input())
arr = list(map(int, input().split()))
arr.sort()
right =1
left = 0
ans = 1
while right < n:
    if arr[right]- arr[left] < 6:
        ans = max(ans, right - left +1)
        right+=1
    else:
        left+=1
        if left == right:
            right +=1
print (ans)
