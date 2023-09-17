class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        largest = 1
        def dfs(node, super_val, direction):
            nonlocal largest
            if node == None:
                return (0, super_val, super_val)
            l, l_min, l_max = dfs(node.left, node.val, 0)
            r, r_min, r_max = dfs(node.right, node.val, 1)
            if l == -1 or r == -1:
                return (-1, -99999, -99999)
            largest = max(largest, l + r + 1)
            if direction == 0 and node.val < super_val and r_max < super_val:
                return (l + r + 1, l_min, r_max)
            elif direction == 1 and node.val > super_val and l_min > super_val:
                return (l + r + 1, l_min, r_max)
            else:
                return (-1, -99999, -99999)
        if root == None:
            return 0
        dfs(root, root.val + 1, 0)
        return largest