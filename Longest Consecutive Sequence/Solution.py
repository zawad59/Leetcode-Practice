class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        bestseq = 0

        for x in nums:
            if x in dict:
                continue
            elem_before = dict.get(x-1, 0)
            elem_after = dict.get(x+1, 0)

            seq_len = elem_before + 1 + elem_after
            bestseq = max(seq_len, bestseq)

            dict[x] = seq_len

            dict[x-elem_before] = seq_len
            dict[x+elem_after] = seq_len

        return bestseq