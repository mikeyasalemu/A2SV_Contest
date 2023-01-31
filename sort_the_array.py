size = int(input())
arr = list(map(int, input().split()))
start =  0
end  = 0
reverse  = False
for i in range(size -1):
    if arr[i] > arr[i +1]:
        
        if not reverse:
            start = i
        reverse = True
    if reverse and arr[i] < arr[i +1]:
        reverse = False
        end  = i
        break
if reverse:
     end = size -1
x = start
y = end 
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
check  = True
for i in range(size -1):
    if arr[i] > arr[i +1]:
        check = False
        print ("no")
        break
if check:
    print("yes")
    print(x + 1, y + 1)
