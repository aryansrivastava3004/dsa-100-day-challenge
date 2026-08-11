class Solution:
    def findRedundantDirectedConnection(self, edges):

        n = len(edges)
        parent = list(range(n + 1))

        candidate1 = None
        candidate2 = None

        # Check if a node has two parents
        for u, v in edges:

            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break

            parent[v] = u

        # Reset Union-Find
        parent = list(range(n + 1))

        def find(x):

            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        for u, v in edges:

            # Skip the second candidate temporarily
            if candidate2 and [u, v] == candidate2:
                continue

            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:

                if candidate1:
                    return candidate1

                return [u, v]

            parent[rootV] = rootU

        return candidate2
