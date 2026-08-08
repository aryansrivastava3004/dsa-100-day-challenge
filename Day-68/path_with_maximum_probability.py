import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        maxProb = [0] * n
        maxProb[start_node] = 1

        heap = [(-1, start_node)]

        while heap:

            probability, node = heapq.heappop(heap)
            probability = -probability

            if node == end_node:
                return probability

            if probability < maxProb[node]:
                continue

            for neighbor, edgeProb in graph[node]:

                newProb = probability * edgeProb

                if newProb > maxProb[neighbor]:
                    maxProb[neighbor] = newProb
                    heapq.heappush(
                        heap,
                        (-newProb, neighbor)
                    )

        return 0
