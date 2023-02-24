n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    num3, num4 = map(int, input().split())
    rotate = 1
    
    check = False
    while rotate < 5:
        if num3 > num1 and num4 > num2 and num1 < num2 and num3 < num4:
            check = True
            break
        else:
            num3, num2  = num2, num3
            num1, num2 =num2, num1
            num3, num4 = num4, num3
            rotate+=1
    if check:
        print("YES")
    else:
        print("NO")
