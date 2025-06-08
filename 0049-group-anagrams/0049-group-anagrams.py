class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        # Use sorted word as the key, because anagrams have the same sorted form.
        # for str in strs:
        #     groups[tuple(sorted(str))].append(str)
        # return list(groups.values())

        # Use character count as the key, since anagrams have the same letter frequency.
        for str in strs:
            count = [0] * 26  

            for char in str:
                count[ord(char) - ord('a')] += 1

            groups[tuple(count)].append(str)

        return list(groups.values())