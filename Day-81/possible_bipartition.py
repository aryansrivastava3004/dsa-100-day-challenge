from collections import deque

class Solution:
    def possibleBipartition(self, n, dislikes):

        graph = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [-1] * (n + 1)

        for person in range(1, n + 1):

            if color[person] != -1:
                continue

            queue = deque([person])
            color[person] = 0

            while queue:

                current = queue.popleft()

                for neighbor in graph[current]:

                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)

                    elif color[neighbor] == color[current]:
                        return False

        return True
