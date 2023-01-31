import collections
size = int(input())
arr = list(map(int, input().split()))
sum1 = 0
sum2 = 0
p1 = size -1
p2 = 0
turn = True
while p2 <= p1:
    if turn:
        if arr[p1] > arr[p2]:
            sum1+= arr[p1]
            p1 -= 1
        else:
            sum1+= arr[p2]
            p2 +=1
        turn = False
    else:
        if arr[p1] > arr[p2]:
            sum2+= arr[p1]
            p1 -= 1
        else:
            sum2+= arr[p2]
            p2 +=1
        turn = True
   
print(sum1, sum2)
        
