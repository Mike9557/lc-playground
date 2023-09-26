class UnionFind:
    def __init__(self, size) -> None:
        self.root = [-1] * (size)
        self.rank = [0] * (size)
        self.count = 0
    def find(self, index) -> int:
        if self.root[index] != index:
            self.root[index] = self.find(self.root[index])
        return self.root[index]
    def island(self, index) -> bool:
        return True if self.root[index] >= 0 else False

    def addland(self, index):
        if(self.root[index] >= 0):
            return
        self.root[index] = index
        self.count += 1

    def union(self, index1, index2) -> None:
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.root[root1] = self.root[root2]
        elif self.rank[root1] < self.rank[root2]:
            self.root[root2] = self.root[root1]
        else:
            self.root[root2] = self.root[root1]
            self.rank[root2] += 1
        self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        uf = UnionFind(m * n)
        result = []
        for position in positions:
            position_index = position[0] * n + position[1]
            uf.addland(position_index)
            for direction in directions:
                neighborx = position[0] + direction[0]
                neighbory = position[1] + direction[1]
                neighbor_index = neighborx * n + neighbory
                if 0 <= neighborx < m and 0 <= neighbory < n and uf.island(neighbor_index):
                    uf.union(position_index, neighbor_index)
            result.append(uf.count)
        return result
            