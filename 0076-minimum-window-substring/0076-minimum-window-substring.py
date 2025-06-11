class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        # Count the frequency of each character in t
        t_count = Counter(t)
        window = defaultdict(int) # Current window character counts
        have, need = 0, len(t_count) # How many required chars matched vs total needed

        res_len = float("inf") # Track the minimum window size found
        res = [-1, -1] # To store the start and end index of the best window
        left = 0 # Left boundary of the window

        # Expand the window by moving the right pointer
        for right, c in enumerate(s):
            window[c] += 1

            # If current char is in t and its count matches, we have one satisfied char
            if c in t_count and window[c] == t_count[c]:
                have += 1

            # Try to shrink the window from the left if it's valid
            while have == need:
                # Update result if this window is smaller than previous best
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove the leftmost character and shrink the window
                left_char = s[left]
                window[left_char] -= 1
                # If the removed character was one of the required characters
                # and its count is now less than what is needed, we lose a match
                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1
                left += 1

        # Return the best window found, or "" if none was valid
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""