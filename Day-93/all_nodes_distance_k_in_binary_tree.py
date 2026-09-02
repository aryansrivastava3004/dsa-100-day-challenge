from collections import defaultdict, deque

class Solution:
    def distanceK(self, root, target, k):

        graph = defaultdict(list)

        def build_graph(node, parent=None):

            if not node:
                return

            if parent:
                graph[node].append(parent)
                graph[parent].append(node)

            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root)

        queue = deque([(target, 0)])
        visited = {target}

        while queue:

            node, distance = queue.popleft()

            if distance == k:
                result = [node.val]

                while queue:
                    next_node, next_distance = queue.popleft()

                    if next_distance == k:
                        result.append(next_node.val)

                return result

            for neighbor in graph[node]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return []
