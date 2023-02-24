size = int(input())
for i in range(size):
    length = int(input())
    string = input()
    check = True
    dic1 = {}
    dic2 = {}
    set1 = set()
    set2 = set()
    ans = 0
    for i in range(length):
        set1.add(string[i])
        dic1[i] = len(set1)
    for j in range(length -1, -1, -1):
        set2.add(string[j])
        dic2[j] = len(set2)
    for i in range(length -1):
        ans = max(dic1[i] + dic2[i+1], ans)
     
    print(ans)
    
