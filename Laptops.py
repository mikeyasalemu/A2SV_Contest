size = int(input())
arr = []
for i in range(size):
    num1, num2 = map(int, input().split())
    arr.append([num1, num2])
arr.sort()
check  = False
for i in range(size -1):
    if  arr[i][1] > arr[i+1][1]:
        print("Happy Alex")
        check = True
        break
if not check:
    print("Poor Alex")
