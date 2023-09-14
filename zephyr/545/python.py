class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def leftBoundary(node) -> List[int]:
            if node == None:
                return []
            if node.left == None and node.right == None:
                return []
            if node.left != None:
                return [node.val] + leftBoundary(node.left)
            else:
                return [node.val] + leftBoundary(node.right)

        def leafBoundary(node) -> List[int]:
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [node.val]
            return leafBoundary(node.left) + leafBoundary(node.right)
            
        
        def rightBoundary(node) -> List[int]:
            if node == None:
                return []
            if node.left == None and node.right == None:
                return []
            if node.right != None:
                return rightBoundary(node.right) + [node.val]
            else:
                return rightBoundary(node.left) + [node.val]

        return [root.val] + leftBoundary(root.left) + leafBoundary(root.left) + leafBoundary(root.right) + rightBoundary(root.right)