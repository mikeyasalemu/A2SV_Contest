import collections
size = int(input())
lst = "codeforces"
lst = set(lst)
for i in range(size):
    c = input()
    if c in lst:
        print("YES")
    else:
        print("NO")
