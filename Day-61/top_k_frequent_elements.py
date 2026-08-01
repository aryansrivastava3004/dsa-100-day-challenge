from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):

        frequency = Counter(nums)

        return heapq.nlargest(
            k,
            frequency.keys(),
            key=frequency.get
        )
