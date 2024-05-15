class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        elementList = {}
        for key, val in enumerate(numbers):
            x = target - val
            if(x in elementList):
                return [elementList[x] + 1, key+1]
            elementList[val] = key