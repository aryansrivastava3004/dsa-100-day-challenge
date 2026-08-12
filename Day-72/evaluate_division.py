from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):

        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):

            if current not in graph or target not in graph:
                return -1.0

            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:

                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1.0:
                    return weight * result

            return -1.0

        answer = []

        for start, end in queries:
            answer.append(dfs(start, end, set()))

        return answer
