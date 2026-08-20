from collections import defaultdict

class Solution:
    def minReorder(self, n, connections):

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = set()

        def dfs(node):
            visited.add(node)
            changes = 0

            for neighbor, cost in graph[node]:

                if neighbor in visited:
                    continue

                changes += cost
                changes += dfs(neighbor)

            return changes

        return dfs(0)
