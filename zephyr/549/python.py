class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        _max = 0
        def longestPath(node) -> list:
            nonlocal _max
            if node == None:
                return [0, 0]
            left = longestPath(node.left)
            right = longestPath(node.right)
            result = [1, 1]
            if left[0] is not 0:
                if node.val - node.left.val == 1:
                    result[0] += left[0]
                if node.left.val - node.val == 1:
                    result[1] += left[1]
            if right[0] is not 0:
                if node.val - node.right.val == 1:
                    result[0] = max(result[0], right[0] + 1)
                if node.right.val - node.val == 1:
                    result[1] = max(result[1], right[1] + 1)
            _max = max(_max, result[0] + result[1] - 1)
            return result
        longestPath(root)