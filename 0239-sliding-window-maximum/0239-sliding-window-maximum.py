class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res= []
        q = deque() # Store indices of useful elements, in decreasing order by value
                    # So nums[q[0]] is always the biggest in the current window

        for i, n in enumerate(nums):
            # Remove indices that are out of the current window
            # Left = (i - k + 1), since k = window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove elements smaller than the current element from the back
            # So we pop them out to keep the queue elements in decreasing order
            # This helps us avoid repeatedly processing smaller numbers that would never matter
            while q and nums[q[-1]] < n:
                q.pop()

            # Add the current element to the back of the queue
            # After popping smaller elements, this guarantees the queue remains decreasing.
            q.append(i)

            # Once we have a full window (i >= k-1), record the max which is at q[0]
            if i >= k - 1:
                res.append(nums[q[0]])
        return res