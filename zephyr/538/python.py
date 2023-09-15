class Solution:
    # better preformance
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        current_sum = 0
        def dfs(node):
            nonlocal current_sum
            if node == None:
                return
            dfs(node.right)
            current_sum += node.val
            node.val = current_sum
            dfs(node.left)
        dfs(root)
        return root
    
# class Solution:
#     # original solution
#     def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         node = root
#         stack = []
#         val_list = []
#         def asdf(node):
#             nonlocal stack
#             nonlocal val_list
#             if node == None:
#                 return
#             stack.append(node)
#             val_list.append(node.val)
#             asdf(node.left)
#             asdf(node.right)
#         asdf(root)
#         val_list.sort()
#         while len(stack) != 0:
#             tmp = stack.pop()
#             tmp.val = sum(val_list[val_list.index(tmp.val):])
#         return root