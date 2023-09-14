class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        _count = 0
        def countUS(node: Optional[TreeNode], master_value: int) -> bool:
            if node == None:
                return True
            nonlocal _count
            left_same = countUS(node.left, node.val)
            right_same = countUS(node.right, node.val)
            if left_same and right_same:
                _count += 1
            else:
                return False
            if node.val != master_value:
                return False
            return True
        if root == None:
            return 0
        countUS(root, root.val)
        return _count