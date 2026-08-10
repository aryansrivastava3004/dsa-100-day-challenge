class Solution:
    def findRedundantConnection(self, edges):

        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

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

        for u, v in edges:

            if not union(u, v):
                return [u, v]
