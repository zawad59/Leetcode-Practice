class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = currentSum
        if(len(nums)==1):
            return nums[0]
        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum
        