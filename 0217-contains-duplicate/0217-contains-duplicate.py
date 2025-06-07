class Solution(object):
    def containsDuplicate(self, nums):
        records = set()
        for num in nums:
            if num in records:
                return True
            records.add(num)
        return False