class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        closest = node.val
        while node != None:
            if node.val == target:
                return node.val
            if node.val > target:
                if abs(closest - target) > abs(node.val - target):
                    closest = node.val
                elif abs(closest - target) == abs(node.val - target):
                    closest = min(closest, node.val)
                node = node.left
            else:
                if abs(closest - target) > abs(node.val - target):
                    closest = node.val
                elif abs(closest - target) == abs(node.val - target):
                    closest = min(closest, node.val)
                node = node.right
        return closest