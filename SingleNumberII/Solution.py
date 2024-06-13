class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counterArr = {}
        for x in nums:
            if(x in counterArr):
                counterArr[x]+=1
            else:
                counterArr[x] = 1
        
        for key, value in counterArr.items():
            if(value == 1):
                return key