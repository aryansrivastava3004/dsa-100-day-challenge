from collections import defaultdict, deque

class Solution:
    def secondMinimum(self, n, edges, time, change):

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist1 = [float('inf')] * (n + 1)
        dist2 = [float('inf')] * (n + 1)

        dist1[1] = 0

        queue = deque([(1, 0)])

        while queue:

            node, currentTime = queue.popleft()

            for neighbor in graph[node]:

                nextTime = currentTime

                cycle = nextTime // change

                if cycle % 2 == 1:
                    nextTime = (cycle + 1) * change

                nextTime += time

                if nextTime < dist1[neighbor]:

                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = nextTime

                    queue.append((neighbor, nextTime))

                elif dist1[neighbor] < nextTime < dist2[neighbor]:

                    dist2[neighbor] = nextTime
                    queue.append((neighbor, nextTime))

            if dist2[n] != float('inf'):
                return dist2[n]
