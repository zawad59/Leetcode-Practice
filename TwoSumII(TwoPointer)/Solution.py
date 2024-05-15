class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        CurSum = 0
        for i in range(0, len(numbers)):
            CurSum = numbers[l] + numbers[r]
            if(CurSum==target):
                return[l+1, r+1]
            elif(CurSum < target):
                l+=1
            elif(CurSum > target):
                r-=1