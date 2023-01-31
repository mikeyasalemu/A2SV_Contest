size = int(input())
for i in range(size):
    string = str(input())
    ans = ""
    left = 0
    while left < len(string):
        if left + 1 < len(string):
            if string[left] == string[left+1]:
                left+=2
            elif string[left] != string[left+1]:
                ans+= string[left]
                left+=1
        else:
            ans+= string[left]
            left+=1
    ans = list(set(ans))   
    ans.sort()
    print("".join(ans))
