class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = len(s1)
        matched = 0   

        for right in range(len(s2)):
            current_char = s2[right]
            if current_char in s1_count: 
                s1_count[current_char] -= 1
                if s1_count[current_char] == 0:
                    matched += 1
            
            if right >= window:
                left_char = s2[right - window]
                if left_char in s1_count: 
                    if s1_count[left_char] == 0:
                        matched -= 1
                    s1_count[left_char] += 1

            if matched == len(s1_count):
                return True

        return False