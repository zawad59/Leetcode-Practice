class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list2 = []
        CurSum = 0
        for i in range(0, len(nums)-1):
            if(i > 0 and nums[i]==nums[i-1]):
                continue
            target = 0 - nums[i]
            l = i+1
            r = len(nums)-1
            while(l < r):
                CurSum = nums[l] + nums[r] 
                if(CurSum==target):
                    list2.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    while(nums[l]==nums[l-1] and l < r):
                        l+=1
                elif(CurSum < target):
                    l+=1
                elif(CurSum > target):
                    r = r - 1
        return list2