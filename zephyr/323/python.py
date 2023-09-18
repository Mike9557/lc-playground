class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]

    def find(self, n: int):
        if n == self.root[n]:
            return n
        self.root[n] = self.find(self.root[n])
        return self.root[n]
    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        # print(uf.root)
        for edge in edges:
            uf.union(edge[0], edge[1])
            # print(uf.root)
        return len(set([uf.find(i) for i in range(n)]))