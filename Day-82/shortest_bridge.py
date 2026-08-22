from collections import deque

class Solution:
    def shortestBridge(self, grid):

        n = len(grid)
        queue = deque()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        found = False

        def dfs(r, c):

            if (
                r < 0 or r >= n or
                c < 0 or c >= n or
                grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            queue.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(n):

            if found:
                break

            for c in range(n):

                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        distance = 0

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n:

                        if grid[nr][nc] == 1:
                            return distance

                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

            distance += 1

        return -1
