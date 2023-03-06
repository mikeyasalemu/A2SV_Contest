n, start, end = map(int, input().split())
nums = list(map(int, input().split()))


def sub_arrays_with_sum_less_than(target):
    runningSum = answer = left = 0

    for right in range(len(nums)):
        runningSum += nums[right]
        print (runningSum)
        while runningSum >= target:
            runningSum -= nums[left]
            left += 1
        answer += right - left + 1
        print(right,answer)
    return answer


print(sub_arrays_with_sum_less_than(end + 1) - sub_arrays_with_sum_less_than(start))