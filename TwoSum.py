class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDic = {}
        for key, val in enumerate(nums):
            x = target - val
            if(x in numsDic):
                return [numsDic[x], key]
            numsDic[val] = key
         