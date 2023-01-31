import collections
size = int(input())
for i in range(size):
    string = str(input())
    one = 0
    two = 0
    three = 0
    left = 0
    ans = float('inf')
    ret = 0
    for right in range(len(string)):
        if string[right] == '1':
            one += 1
        elif string[right] == '2':
            two += 1
        elif string[right] == '3':
            three += 1
            
        while one > 0 and two > 0 and three > 0:
            if string[left] == '1':
                one -= 1
            elif string[left] == '2':
                two -= 1
            elif string[left] == '3':
                three -= 1
            ans = min(ans, right - left + 1)
            ret = ans
            left +=1
        
        
    print(ret)

        
