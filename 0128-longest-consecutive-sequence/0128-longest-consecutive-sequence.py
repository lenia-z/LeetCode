class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                res = max(length, res)
        
        return res