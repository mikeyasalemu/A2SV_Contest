size = int(input())
lst = list(map(str, input().split(" ")))
string = ""
lst2  = []
size2 = int(input())
for i in range(size2):
    string = str(input())
    lst2.append(string)
lst2.sort()
j = 0
for i in range(size2):
    while  j < size and lst2[i] > lst[j]:
        j+=1
    print(j)
        