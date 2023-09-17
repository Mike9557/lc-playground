class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_length = 0
        def dfs(node):
            nonlocal max_length
            if node == None:
                return 0
            if len(node.children) == 0:
                return 1
            lengths = [dfs(child) for child in node.children]
            lengths.sort(reverse=True)
            max_length = max(sum(lengths[:2]), max_length)
            return lengths[0] + 1
        dfs(root)
        return max_length