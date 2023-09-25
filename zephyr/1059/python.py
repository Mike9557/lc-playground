class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        directed_map = {}
        loop_signal = False
        end_but_not_destination = False
        node_check = [False] * n
        for edge in edges:
            directed_map.setdefault(edge[0], [])
            directed_map.setdefault(edge[1], [])
            directed_map[edge[0]].append(edge[1])
        def dfs(s, step: List[int]):
            nonlocal loop_signal
            nonlocal directed_map
            nonlocal node_check
            nonlocal end_but_not_destination
            if node_check[s]:
                return
            if loop_signal or end_but_not_destination:
                return
            if step[s]:
                loop_signal = True
                return
            if s != destination and len(directed_map[s]) == 0:
                end_but_not_destination = True
                return
            if s == destination and len(directed_map[s]) == 0:
                node_check[s] = True
                return
            step[s] = True
            for l in directed_map[s]:
                dfs(l, step)
            step[s] = False
            node_check[s] = True
            if loop_signal or end_but_not_destination:
                node_check[s] = True
                return
        if len(edges) == 0 and source == destination:
            return True
        if len(edges) == 0:
            return False
        dfs(source, [False] * n)
        return not loop_signal and not end_but_not_destination
            
