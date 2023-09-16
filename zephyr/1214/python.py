# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def BS(num, node):
            nonlocal find_sol
            if find_sol:
                return
            if node == None:
                return
            if num + node.val == target:
                find_sol = True
                return
            elif num + node.val > target:
                BS(num, node.left)
            else:
                BS(num, node.right)
        
        def dfs(node):
            nonlocal find_sol
            if node == None:
                return
            if find_sol:
                return

            dfs(node.left)
            BS(node.val, root2)
            dfs(node.right)
        
        find_sol = False

        dfs(root1)
        return find_sol
