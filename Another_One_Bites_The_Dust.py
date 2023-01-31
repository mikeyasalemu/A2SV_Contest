from collections import Counter
import math
nums = list(map(int, input().split()))
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]
diff = abs(num1 -num2)
minn = min (num1 , num2)
if diff > 1:
    ans = minn + minn + 1 + (2*num3)
else:
    ans = num1 + num2 + (2*num3)
print(ans)
