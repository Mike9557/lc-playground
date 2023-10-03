class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        gates = collections.deque([])
        for i, room in enumerate(rooms):
            for j, r in enumerate(room):
                if r == 0:
                    gates.append([i, j, 0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while gates:
            gate = gates.popleft()
            for direction in directions:
                dest_x = gate[0] + direction[0]
                dest_y = gate[1] + direction[1]
                if not(0 <= dest_x < len(rooms) and 0 <= dest_y < len(rooms[0])):
                    continue
                if rooms[dest_x][dest_y] == -1:
                    continue
                if rooms[dest_x][dest_y] < gate[2] + 1:
                    continue
                rooms[dest_x][dest_y] = gate[2] + 1
                gates.append([dest_x, dest_y, gate[2] + 1])
        