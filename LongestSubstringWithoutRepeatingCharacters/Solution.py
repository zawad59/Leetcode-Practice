class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        l = 0
        r = 0
        maxLen = 0
        while(r < len(s)):
            if(s[r] in hashMap):
                l = max(l, hashMap[s[r]] + 1)
            hashMap[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r = r + 1
        return maxLen