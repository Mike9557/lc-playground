class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def dfs(node):
            if node == None:
                return None
            subresult = Node()
            subresult.val = node.val
            subresult.children = [dfs(child) for child in node.children]
            return subresult
        return dfs(root)
    
    # shameless way to do it
    def cloneTree2(self, root: 'Node') -> 'Node':
        return copy.deepcopy(root)