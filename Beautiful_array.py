size = int(input())
arr = list(map(int, input().split()))
arr1= []
arr2= []
arr3= []

i = 0

while len(arr) > 0:
    if arr[i] < 0 and len(arr1) % 2 == 0:
        arr1.append(arr.pop(i))
    elif arr[i] > 0:
        arr2.append(arr.pop(i))
    elif arr[i] == 0:
        arr3.append(arr.pop(i))
    elif i +1 < len(arr):
        if arr[i] < 0 and arr[i+1] < 0:
            arr2.append(arr.pop(i+1))
            arr2.append(arr.pop(i))
            i+=1
    elif len(arr3) > 0:
        arr3.append(arr.pop(i))
    i +=1
    if i >= len(arr):
        i = 0
    
print (len(arr1), *arr1)
print (len(arr2), *arr2)
print (len(arr3), *arr3)

            
