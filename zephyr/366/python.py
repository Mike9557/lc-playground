class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        super_root = TreeNode()
        super_root.left = root
        def asdf(node):
            if node == None:
                return False
            if node.left == None and node.right == None:
                return True
            left = asdf(node.left)
            right = asdf(node.right)
            nonlocal tmp
            if left:
                tmp.append(node.left.val)
                node.left = None
            if right:
                tmp.append(node.right.val)
                node.right = None
            return False
        result = []
        while super_root.left != None:
            tmp = []
            asdf(super_root)
            result.append(tmp)
        return result