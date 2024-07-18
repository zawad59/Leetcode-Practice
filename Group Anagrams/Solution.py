class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        finalList = []
        for x in strs:
            sorted_str = str(sorted(x))
            hashMap[sorted_str].append(x)
        for key, value in hashMap.items():
            finalList.append(value)
        return finalList
