n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = 0

for i in range(n -1):
    if arr1[i] + arr1[i+1] > arr2[i] + arr2[i+1]:
        ans +=1
print (ans)