class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xoResult = 0
        for x in nums:
            xoResult = xoResult ^ x
        diff_bit = 1
        
	while not(xoResult & diff_bit):
            diff_bit = diff_bit << 1

        a, b = 0,0
        for n in nums:
            if(diff_bit & n):
                a = a ^ n
            else:
                b = b ^ n
        return [a, b]