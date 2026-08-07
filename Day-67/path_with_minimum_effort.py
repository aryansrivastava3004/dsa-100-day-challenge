import heapq

class Solution:
    def minimumEffortPath(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        heap = [(0, 0, 0)]
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0

        while heap:

            diff, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return diff

            if diff > effort[r][c]:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    newDiff = max(
                        diff,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    if newDiff < effort[nr][nc]:

                        effort[nr][nc] = newDiff
                        heapq.heappush(heap, (newDiff, nr, nc))
