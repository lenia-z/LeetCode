class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            # Since the array is sorted,
            # No need to continue if the current number is greater than zero
            if nums[i] > 0:
                break

            # Skip duplicate to avoid duplicate triplets in the result
            if i > 0 and n == nums[i-1]:
                continue
            
            # Two pointer - two Sum II
            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = n + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1 
                elif current_sum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])

                    # Skip duplicate elements for the left pointer
                    # Right pointer are handled by the current sum logic
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
        return res