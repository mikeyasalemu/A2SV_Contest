n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if len(set(arr))== 1:
        print(-1)
else:
    print(*arr)
# arr1= []
# arr2 = []

# for i in range(n):
#     arr1.append(arr[i])
# for i  in range(n, n*2):
#     arr2.append(arr[i])
# if len(set(arr))== 1:
#     print(-1)
# elif sum(arr1) != sum(arr2):
#     print (*arr)
# else:
#     check = True
#     i = 0
#     j = 0 
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] != arr2[j]:
#             arr1[i], arr2[j] = arr2[j], arr1[i]
            
#         i+=1
#         j+=1
#     if sum(arr1) != sum(arr2):
#         arr1+= arr2
#         print(arr1)
#     else:
#         print(-1)


