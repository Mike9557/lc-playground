class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        _max = 0
        def avgSubtree(node: Optional[TreeNode]):
            if node == None:
                return (0, 0)
            left = avgSubtree(node.left)
            right = avgSubtree(node.right)
            result = ((node.val + left[0] + right[0]), 1 + left[1] + right[1])
            nonlocal _max
            _max = max(_max, result[0] / result[1])
            return result
        avgSubtree(root)
        return _max