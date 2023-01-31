
size = int(input())
for i in range(size):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
   
    if arr1[0] == arr2[0] and arr1[1] + arr2[1] == arr1[0]:
        print('Yes')
    elif arr1[1] == arr2[0] and arr1[0] + arr2[1] == arr1[1]:
        print('Yes')
    elif arr1[0] == arr2[1] and  arr1[1] + arr2[0] == arr2[1]:
        print('Yes')
    elif arr1[1] == arr2[1] and  arr1[0] + arr2[0] == arr2[1]:
        print('Yes')
    else:
        print('No')
