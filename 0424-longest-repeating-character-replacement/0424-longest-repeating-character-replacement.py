class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq, max_len = 0, 0
        left = 0

        for right in range(len(s)):
            # Add the current character to the window count
            # Update the most frequent character count
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # Shrink the window from the left when need to change more than k characters
            while (right -left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # Update the max length if this window is bigger than what have before
            max_len = max(max_len, right - left + 1)

        return max_len