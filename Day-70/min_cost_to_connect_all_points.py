import heapq

class Solution:
    def minCostConnectPoints(self, points):

        n = len(points)

        visited = set()
        heap = [(0, 0)]
        totalCost = 0

        while len(visited) < n:

            cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            totalCost += cost

            x1, y1 = points[node]

            for nextNode in range(n):

                if nextNode not in visited:

                    x2, y2 = points[nextNode]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    heapq.heappush(
                        heap,
                        (distance, nextNode)
                    )

        return totalCost
