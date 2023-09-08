# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        d = {} 
        def helper(node,height):
            if node.left == None and node.right == None:
                if height in d.keys():
                    d[height] += node.val
                else:
                    d[height] = node.val
            elif node.right == None and node.left != None:
                helper(node.left,height+1)
            elif node.right != None and node.left == None:
                helper(node.right,height+1)
            else:
                helper(node.left,height+1)
                helper(node.right,height+1)
        helper(root,0)
        key = max(d)
        return d[key]
    
            