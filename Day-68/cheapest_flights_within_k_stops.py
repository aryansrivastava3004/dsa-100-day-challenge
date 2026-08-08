from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        heap = [(0, src, 0)]
        best = {}

        while heap:

            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            state = (node, stops)

            if state in best and best[state] <= cost:
                continue

            best[state] = cost

            for neighbor, price in graph[node]:

                newCost = cost + price

                heapq.heappush(
                    heap,
                    (newCost, neighbor, stops + 1)
                )

        return -1
