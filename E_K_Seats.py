row, column, k = map(int, input().split())
arr = []
count2 = 0
for i in range(row):
    string = list(str(input()))
    arr.append(string)
    count = 0
    for i in range(column):
        if string[i] == ".":
            count +=1
            if count >= k:
                count2+=1
        else:
            count = 0        
if k != 0:
    for i in range(column):
        count = 0
        for j in range(row):
            if arr[j][i] == ".":
                count += 1
                if count >= k:
                    count2+=1
            else:
                count = 0
           
print (count2)
