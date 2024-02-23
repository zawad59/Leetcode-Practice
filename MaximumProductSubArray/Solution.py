class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        product = 1
        temp = 0
        max1 = temp
        for i in range(0, len(nums)):
            product = product * nums[i]
            temp = max(product, temp, nums[i])    
            if(nums[i]==0):
                max1 = temp
                product = 1
        forward = max(max1,temp)
        x = len(nums)-1
        product = 1
        while(x>=0):
              product = product * nums[x] 
              temp = max(product, temp, nums[x])
              if(nums[x]==0):
                max1 = temp
                product = 1
              x-=1
        backward = max(max1,temp)
        return max(forward,backward)
            