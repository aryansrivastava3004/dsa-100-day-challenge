from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):

        rows = len(maze)
        cols = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, steps = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    maze[nr][nc] == "."
                ):

                    newSteps = steps + 1

                    if (
                        nr == 0 or
                        nr == rows - 1 or
                        nc == 0 or
                        nc == cols - 1
                    ):
                        return newSteps

                    maze[nr][nc] = "+"
                    queue.append((nr, nc, newSteps))

        return -1
