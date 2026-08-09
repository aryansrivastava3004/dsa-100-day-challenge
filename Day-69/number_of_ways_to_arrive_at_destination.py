import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n, roads):

        graph = defaultdict(list)

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        MOD = 10**9 + 7

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:

            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:

                newTime = time + weight

                if newTime < dist[neighbor]:

                    dist[neighbor] = newTime
                    ways[neighbor] = ways[node]

                    heapq.heappush(
                        heap,
                        (newTime, neighbor)
                    )

                elif newTime == dist[neighbor]:

                    ways[neighbor] = (
                        ways[neighbor] + ways[node]
                    ) % MOD

        return ways[n - 1]
