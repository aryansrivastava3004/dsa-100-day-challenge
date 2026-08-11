class Solution:
    def makeConnected(self, n, connections):

        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        rank = [1] * n

        def find(x):

            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(a, b):

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA
            rank[rootA] += rank[rootB]

            return True

        components = n

        for u, v in connections:

            if union(u, v):
                components -= 1

        return components - 1
