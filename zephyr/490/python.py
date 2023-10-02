class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def move(position):
            nonlocal maze
            if position[0] < 0 or position[0] >= len(maze) or position[1] < 0 or position[1] >= len(maze[0]):
                return False
            if maze[position[0]][position[1]] == 1:
                return False
            return True
        
        def is_in_destionation(position):
            if position[0] == destination[0] and position[1] == destination[1]:
                return True
            else:
                return False

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = collections.deque()
        q.append(start)
        steps = {}
        steps[tuple(start)] = 0
        while q:
            point = q.popleft()
            step = steps[tuple(point)]
            for direction in directions:
                predict_point = [point[0], point[1]]

                while move((predict_point[0] + direction[0], predict_point[1] + direction[1])):
                    predict_point[0], predict_point[1] = predict_point[0] + direction[0], predict_point[1] + direction[1]

                if is_in_destionation(predict_point):
                    return True

                if tuple(predict_point) in steps and steps[tuple(predict_point)] <= step + 1:
                    continue
                q.append(predict_point)
                steps[tuple(predict_point)] = step + 1
        return False