class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i