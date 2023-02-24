size = int(input())
for i in range(size):
    length = int(input())
    string = input()
    left = 0
    right = length - 1
    ans = 0
    while right >= left:
        if string[left] == string[right]:
            ans = right - left + 1
            break
        right -=1
        left +=1
    print(ans)
