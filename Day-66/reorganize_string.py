from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s):

        frequency = Counter(s)

        heap = [(-count, char) for char, count in frequency.items()]
        heapq.heapify(heap)

        result = []

        prevCount = 0
        prevChar = ""

        while heap:

            count, char = heapq.heappop(heap)

            result.append(char)

            if prevCount < 0:
                heapq.heappush(heap, (prevCount, prevChar))

            count += 1
            prevCount = count
            prevChar = char

        answer = "".join(result)

        return answer if len(answer) == len(s) else ""
