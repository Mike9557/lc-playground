class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [0] * n

    def union(self, x, y) -> None:
        self.root[x - 1]

class Solution:
    # Editorial Solution
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        in_count = {i: 0 for i in range(1, n + 1)}
        for x, y in relations:
            graph[x].append(y)
            in_count[y] += 1
        queue = []
        for node in graph:
            if in_count[node] == 0:
                queue.append(node)
        
        step = 0
        studied_count = 0
        while queue:
            step += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    if in_count[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue
        return step if studied_count == n else -1