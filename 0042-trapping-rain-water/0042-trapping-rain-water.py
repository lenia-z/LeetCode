class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                # Update the highest left bar so far
                # Water at left pointer = l_max - height[l] 
                # safe since l_max ≥ height[l]
                l_max = max(l_max, height[l])
                water += l_max - height[l]
                l += 1
            else:
                # Update the highest right bar so far
                # Water at right pointer = r_max - height[r] 
                # safe since r_max ≥ height[r]
                r_max = max(r_max, height[r])
                water += r_max - height[r]
                r -= 1
        return water