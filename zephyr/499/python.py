class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        def move(position):
            nonlocal maze
            if position[0] < 0 or position[0] >= len(maze) or position[1] < 0 or position[1] >= len(maze[0]):
                return False
            if maze[position[0]][position[1]] == 1:
                return False
            return True
        
        def is_in_destionation(position):
            if position[0] == hole[0] and position[1] == hole[1]:
                return True
            else:
                return False

        if ball == hole:
            return ''
        direction_labels = ['u', 'l', 'd', 'r']
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = collections.deque()
        q.append(ball)
        steps = {}
        steps[tuple(ball)] = [0, '']
        steps[tuple(hole)] = [-1, 'impossible']
        while q:
            point = q.popleft()
            step = steps[tuple(point)][0]
            step_label = steps[tuple(point)][1]
            if point == [4, 8]:
                print('here')
            if steps[tuple(hole)][0] != -1 and steps[tuple(hole)][0] < step:
                continue
            for i, direction in enumerate(directions):
                predict_point = [point[0], point[1]]
                tmp_step = 0
                while move((predict_point[0] + direction[0], predict_point[1] + direction[1])):
                    predict_point[0], predict_point[1] = predict_point[0] + direction[0], predict_point[1] + direction[1]
                    tmp_step += 1
                    if is_in_destionation(predict_point):
                        if steps[tuple(hole)][1] == 'impossible':
                            steps[tuple(hole)][0] = step + tmp_step
                            steps[tuple(hole)][1] = step_label + direction_labels[i]
                        break
                if tmp_step == 0:
                    continue
                if tuple(predict_point) in steps and steps[tuple(predict_point)][0] < step + tmp_step:
                    continue
                elif tuple(predict_point) in steps and steps[tuple(predict_point)][0] == step + tmp_step:
                    if steps[tuple(predict_point)][1] > step_label + direction_labels[i]:
                        steps[tuple(predict_point)][1] = step_label + direction_labels[i]
                        q.append(predict_point)
                elif tuple(predict_point) in steps and steps[tuple(predict_point)][0] > step + tmp_step:
                    steps[tuple(predict_point)][0] = step + tmp_step
                    steps[tuple(predict_point)][1] = step_label + direction_labels[i]
                    q.append(predict_point)
                else:
                    steps.setdefault(tuple(predict_point), [step + tmp_step, step_label + direction_labels[i]])
                    q.append(predict_point)
        return steps[tuple(hole)][1]