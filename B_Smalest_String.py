n = int(input())
for i in range(n):
    sizeA, sizeB, k = map(int, input().split())
    arr1 = list(str(input()))
    arr2 = list(str(input()))
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    ans = ""
    count = 0 
    if arr1[i] <= arr2[j]:
         check = True
    else:
        check = False
    while i < len(arr1) and j < len(arr2):
        if  check:
            ans += arr1[i]
            i +=1 
            count +=1
            while count < k:
                if i < len(arr1) and arr1[i] <= arr2[j]:
                    ans += arr1[i]
                    i += 1
                count+=1
            count = 0
            check = False
        else:
            ans += arr2[j]
            j += 1
            count+=1
            while count < k:
                print
                if j < len(arr2) and arr2[j] <= arr1[i]:
                    ans += arr2[j]
                    j += 1
                count+=1
            count = 0 
            check = True
            
    print (ans)
