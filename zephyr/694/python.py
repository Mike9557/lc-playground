class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n = len(grid)
        m = len(grid[0])
        def dfs(x: int, y: int, lx, ly) -> int:
            nonlocal grid
            nonlocal directions

            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            current_island.add((lx, ly))
            for direction in directions:
                if 0 <= x + direction[0] < n and 0 <= y + direction[1] < m:
                    dfs(x + direction[0], y + direction[1], lx + direction[0], ly + direction[1])
        
        unique_island = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_island = set()
                tmp_hash = dfs(i, j, 0, 0)
                if tmp_hash == 0:
                    continue
                unique_island.add(frozenset(current_island))
        return len(unique_island)