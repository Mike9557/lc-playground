class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        x = abs(x) + 3
        y = abs(y) + 3
        directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (2, -1), (1, -2), (1, 2), (2, 1)]
        q = collections.deque([[3, 3, 0]])
        visited = [[0 for _ in range(y + 3)] for _ in range(x + 3)]
        steps = [[max(3, x * y) for _ in range(y + 6)] for _ in range(x + 6)]
        min_count = 0
        while q:
            tmpx, tmpy, count = q.popleft()
            if visited[tmpx][tmpy] != 0:
                continue
            visited[tmpx][tmpy] = 1
            steps[tmpx][tmpy] = count
            for direction in directions:
                dest_x = tmpx + direction[0]
                dest_y = tmpy + direction[1]
                if 0 > dest_x or dest_x > x + 2 or 0 > dest_y or dest_y > y + 2:
                    continue
                if dest_x == x and dest_y == y:
                    return count + 1
                if visited[dest_x][dest_y] == 1:
                    continue
                steps[dest_x][dest_y] = count + 1
                q.append([dest_x, dest_y, count + 1])