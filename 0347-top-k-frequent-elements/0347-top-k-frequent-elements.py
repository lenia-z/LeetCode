class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = Counter(nums)
        
        # Count frequencies of each element.
        # Create buckets indexed by frequency.
        # Collect elements from highest frequency down until k elements are gathered.
        '''
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range (len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        '''

        # Count frequencies.
        # Build a heap using negative frequencies.
        # Pop k elements with highest frequency from the heap.
        '''
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res
        '''

        # Using heapq.nlargest (built-in function).
        # Return k numbers with highest frequency using nlargest.
        return heapq.nlargest(k, count.keys(), key = count.get)