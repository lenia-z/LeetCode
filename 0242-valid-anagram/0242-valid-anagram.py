class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # This method uses built-in Counter to count the frequency of each character.
        # If both strings have identical frequency maps, they are anagrams.
        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        # First count the frequency of each character in string s.
        # Then for each character in string t, reduce the frequency.
        # If a character in t doesn't exist or runs out, return False.
        # Otherwise, they are anagrams.
        # freq = {}

        # for char in s:
        #     freq[char] = freq.get(char, 0) + 1

        # for char in t:
        #     if freq.get(char, 0) > 0:
        #         freq[char] -= 1
        #     else:
        #         return False

        # return True

        # Count frequencies of both strings.
        # Then compare both dictionaries key by key.
        # If any character has a different count, return False. 
        # Otherwise, they are anagrams.
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False

        return True