from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):

        frequency = Counter(tasks)

        maxFreq = max(frequency.values())
        maxCount = list(frequency.values()).count(maxFreq)

        return max(
            len(tasks),
            (maxFreq - 1) * (n + 1) + maxCount
        )
