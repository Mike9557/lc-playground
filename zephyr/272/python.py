class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        sorted_list = []
        def dfs(node):
            nonlocal sorted_list
            if node == None:
                return
            dfs(node.left)
            sorted_list.append(node.val)
            dfs(node.right)
        dfs(root)
        sorted_list.sort(key= lambda x : abs(target - x))
        return sorted_list[:k]