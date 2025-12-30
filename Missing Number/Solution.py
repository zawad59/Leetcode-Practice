class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumTotal = n * (n+1)
        sumTotal = sumTotal/2

        sum_Arr = sum(nums)

        missingElement = int(sumTotal - sum_Arr)

        return missingElement
        