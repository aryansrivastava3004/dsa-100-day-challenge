from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):

        frequency = Counter(words)

        heap = [(-count, word) for word, count in frequency.items()]
        heapq.heapify(heap)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
