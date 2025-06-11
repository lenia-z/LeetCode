class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1) # Count the frequency of each character in s1
        window = len(s1) # Fixed window size, must match the length of s1
        matched = 0 # Number of characters fully matched in s2

        for right in range(len(s2)):
            current_char = s2[right]

            # If the current character is in the target, try to match it
            if current_char in s1_count: 
                s1_count[current_char] -= 1
                # Fully matched this character
                if s1_count[current_char] == 0:
                    matched += 1

            # Once the window is full, start sliding by removing the leftmost character
            if right >= window:
                left_char = s2[right - window] # Character exiting the window
                if left_char in s1_count: 
                    # If it was fully matched before, undo the match
                    # Since the window if fixed, remove the left character even it is matched before
                    # And restore its count in s1_count
                    if s1_count[left_char] == 0:
                        matched -= 1
                    s1_count[left_char] += 1

            # If all characters are fully matched, return True
            if matched == len(s1_count):
                return True

        return False