n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
arr2.sort()
i = 0
j = 0
count = 0
while i < len(arr) and j < len(arr2):
    if arr[i] == arr2[j] or arr[i] + 1 == arr2[j] or arr[i]  == arr2[j] +1:
        count +=1
        i+=1
        j+=1
    elif arr[i] < arr2[j]:
        i +=1
    else:
        j+=1
print(count)