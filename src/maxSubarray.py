
def maxSubArray(nums) -> int:
    curSum = nums[0]
    for i in range(1, len(nums)):
        curSum = max(nums[i], curSum + nums[i])
        if curSum > nums[i]:
            nums[i] = curSum
    return max(nums)




print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(maxSubArray([-1,0,-2]) == 0)
print(maxSubArray([-2,1]) == 1)
print(maxSubArray([5,4,-1,7,8]) == 23)
print(maxSubArray([1]) == 1)
print(maxSubArray([-2,-1]) == -1)