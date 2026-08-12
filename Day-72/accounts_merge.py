class Solution:
    def accountsMerge(self, accounts):

        parent = {}
        rank = {}

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if rank[rootA] < rank[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA

            if rank[rootA] == rank[rootB]:
                rank[rootA] += 1

        for account in accounts:

            firstEmail = account[1]

            if firstEmail not in parent:
                parent[firstEmail] = firstEmail
                rank[firstEmail] = 0

            for email in account[2:]:

                if email not in parent:
                    parent[email] = email
                    rank[email] = 0

                union(firstEmail, email)

        groups = {}

        for email in parent:

            root = find(email)

            if root not in groups:
                groups[root] = []

            groups[root].append(email)

        result = []

        for account in accounts:

            name = account[0]
            root = find(account[1])

            if root in groups:

                result.append(
                    [name] + sorted(groups[root])
                )

                del groups[root]

        return result
