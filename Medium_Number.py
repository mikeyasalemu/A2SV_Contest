size = int(input())
for i in range(size):
    lst = list(map(int , input().split()))
    lst.sort()
    print(lst[1])
