from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):

        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        genes = "ACGT"

        while queue:

            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(len(gene)):

                for char in genes:

                    if char == gene[i]:
                        continue

                    newGene = gene[:i] + char + gene[i + 1:]

                    if newGene in bank and newGene not in visited:
                        visited.add(newGene)
                        queue.append(
                            (newGene, mutations + 1)
                        )

        return -1
