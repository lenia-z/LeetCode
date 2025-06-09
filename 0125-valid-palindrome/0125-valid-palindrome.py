class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric and convert to lowercase
        # # Check if the filtered string is the same as its reverse
        '''
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]
        '''

        # Two Pointers
        # Skip non-alphanumeric characters from both left and right
        # Compare lowercased characters
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True