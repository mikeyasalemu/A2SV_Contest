size = int(input())
for  i in range(size):
    length = input()
    string = str(input())
    
    up = 0
    left = 0
    check = False
    for j in string:
        if j == 'U':
            up+=1
        elif j == 'D':
            up -=1
        elif j == 'R':
            left +=1
        elif j == 'L':
            left -= 1
        
        if left == 1 and up == 1:
            print("YES")
            check = True
            break

    if  not check:
        print("NO")