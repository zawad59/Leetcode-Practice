class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
 
        while low <= high:
             mid = (high + low) // 2
             if(target == nums[mid]):
                 return mid
             if(nums[low] <= nums[mid]):
                 if(target > nums[low] and target > nums[mid]):
                     low = mid + 1
                 elif(target < nums[low] and target < nums[mid]):
                     low = mid + 1
                 else:
                     high = mid - 1
             else:
                 if(target <= nums[high] and target > nums[mid]):
                     low = mid + 1
                 else:
                     high = mid - 1         
        return -1