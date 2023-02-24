from collections import defaultdict
from collections import Counter
size, num = map(int, input().split())
arr = list(map(int, input().split()))
items = []
for i in range(num):
    items.append(input())
arr.sort()
count = Counter(items)
minn = 0
maxx = 0
arr2 = []
for values, items in count.items():
    arr2.append(items)
arr2.sort(reverse = True)
j = len(arr) -1
for i in range(len(arr2)):
    minn += arr2[i] * arr[i]
    maxx += arr2[i] * arr[j]
    j-=1
print(minn, maxx)
